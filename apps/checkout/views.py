from oscar.apps.checkout import views
from oscar.apps.payment import models 
from oscar.core.loading import get_model,get_class
from sms.views import send_sms
from sms.models import Unsent_Sms,Sent_Sms,Starred_Sms
Source=get_model("payment","Source")
SourceType=get_model("payment","SourceType")
import requests
# Subclass the core Oscar view so we can customise
class PaymentDetailsView(views.PaymentDetailsView):

    def handle_payment(self,order_number, total, **kwargs):
        amount = self.request.session['amount']
        receipt = self.request.session['receipt'] 
        phone_number = self.request.session['phone_number']
        message="Hi your order:{order_number} has been received by Roselian cakes.".format(**locals()) 
        # Talk to payment gateway.  If unsuccessful/error, raise a
        # PaymentError exception which we allow to percolate up to be caught
        # and handled by the core PaymentDetailsView.
        try:
            request=send_sms(phone_number,message)
            request=request.json()
            errorcode=request.get('ErrorCode')
            if errorcode==0:
                data=request.get('Data')[0]
                number=data.get('MobileNumber')
                message_id=data.get('MessageId')
                sent=Sent_Sms(phone_number=number,message_id=message_id)
                sent.save()
            else:
                error_code=request.get('ErrorCode')
                error_description=request.get('ErrorDescription')
                data=request.get('Data')[0]
                number=data.get('MobileNumber')
                message_id=data.get('MessageId')
                unsent=Starred_Sms(error_code=error_code,error_description=error_description,mobile_number=number,message_id=message_id,message=message)
                unsent.save()
        except Exception as e:
            unsent=Unsent_Sms(message=message,error=e,station="order",phone_number=number,)
        finally:   
            reference = receipt
            # # Payment successful! Record payment source
            source_type ,is_created=SourceType.objects.get_or_create(name="Lipa_Na_Mpesa")
            source =Source(
                source_type=source_type,
                amount_allocated=amount,
                reference=reference)
            self.add_payment_source(source)
            # Record payment event
            self.add_payment_event('pre-auth',amount,reference=reference)