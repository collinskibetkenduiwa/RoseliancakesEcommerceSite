Run manage.py check --deploy¶ and write report on the same indicating date and author.Screenshots are welcomed and appreciated 
Some of the checks described below can be automated using the check --deploy option. Be sure to run it against your production settings file as described in the option’s documentation.

# 1-Critical settings¶
a-SECRET_KEY¶
The secret key must be a large random value and it must be kept secret.

Make sure that the key used in production isn’t used anywhere else and avoid committing it to source control. This reduces the number of vectors from which an attacker may acquire the key.

Instead of hardcoding the secret key in your settings module, consider loading it from an environment variable:

b-DEBUG¶
You must never enable debug in production.

You’re certainly developing your project with DEBUG = True, since this enables handy features like full tracebacks in your browser.

For a production environment, though, this is a really bad idea, because it leaks lots of information about your project: excerpts of your source code, local variables, settings, libraries used, etc.

Environment-specific settings¶
c-ALLOWED_HOSTS¶
When DEBUG = False, Django doesn’t work at all without a suitable value for ALLOWED_HOSTS.

This setting is required to protect your site against some CSRF attacks. If you use a wildcard, you must perform your own validation of the Host HTTP header, or otherwise ensure that you aren’t vulnerable to this category of attacks.

You should also configure the Web server that sits in front of Django to validate the host. It should respond with a static error page or ignore requests for incorrect hosts instead of forwarding the request to Django. This way you’ll avoid spurious errors in your Django logs (or emails if you have error reporting configured that way). For example, on nginx you might setup a default server to return “444 No Response” on an unrecognized host:


# CACHES¶
If you’re using a cache, connection parameters may be different in development and in production. Django defaults to per-process local-memory caching which may not be desirable.

Cache servers often have weak authentication. Make sure they only accept connections from your application servers.

# DATABASES¶
Database connection parameters are probably different in development and in production.

Database passwords are very sensitive. You should protect them exactly like SECRET_KEY.

For maximum security, make sure database servers only accept connections from your application servers.

critical databases should have a backup

# EMAIL_BACKEND and related settings¶
If your site sends emails, these values need to be set correctly.

By default, Django sends email from webmaster@localhost and root@localhost. However, some mail providers reject email from these addresses. To use different sender addresses, modify the DEFAULT_FROM_EMAIL and SERVER_EMAIL settings.

# STATIC_ROOT and STATIC_URL¶
Static files are automatically served by the development server. In production, you must define a STATIC_ROOT directory where collectstatic will copy them.

See Managing static files (e.g. images, JavaScript, CSS) for more information.

# MEDIA_ROOT and MEDIA_URL¶
Media files are uploaded by your users. They’re untrusted! Make sure your web server never attempts to interpret them. For instance, if a user uploads a .php file, the web server shouldn’t execute it.

Now is a good time to check your backup strategy for these files.

# HTTPS¶
Any website which allows users to log in should enforce site-wide HTTPS to avoid transmitting access tokens in clear. In Django, access tokens include the login/password, the session cookie, and password reset tokens. (You can’t do much to protect password reset tokens if you’re sending them by email.)

Protecting sensitive areas such as the user account or the admin isn’t sufficient, because the same session cookie is used for HTTP and HTTPS. Your web server must redirect all HTTP traffic to HTTPS, and only transmit HTTPS requests to Django.

Once you’ve set up HTTPS, enable the following settings.

# CSRF_COOKIE_SECURE¶
Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.

SESSION_COOKIE_SECURE¶
Set this to True to avoid transmitting the session cookie over HTTP accidentally.

# Performance optimizations¶
Setting DEBUG = False disables several features that are only useful in development. In addition, you can tune the following settings.

# Sessions¶
Consider using cached sessions to improve performance.

If using database-backed sessions, regularly clear old sessions to avoid storing unnecessary data.

# CONN_MAX_AGE¶
Enabling persistent database connections can result in a nice speed-up when connecting to the database accounts for a significant part of the request processing time.

This helps a lot on virtualized hosts with limited network performance.

# TEMPLATES¶
Enabling the cached template loader often improves performance drastically, as it avoids compiling each template every time it needs to be rendered. See the template loaders docs for more information.

# Error reporting¶

LOGGING¶


ADMINS and MANAGERS¶
ADMINS will be notified of 500 errors by email.

MANAGERS will be notified of 404 errors. IGNORABLE_404_URLS can help filter out spurious reports.

See Error reporting for details on error reporting by email.

Error reporting by email doesn’t scale very well

error monitoring system such as Sentry before your inbox is flooded by reports. Sentry can also aggregate logs.

Customize the default error views¶

# Security Alert
# logging,storing and visualizing server metrics
# Serve side security
