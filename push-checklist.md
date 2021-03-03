---
title: "RoselianCakes  Checklist"
---
Prior to pushing changes to Gitlab.com, walk through these items and ensure they are addressed.

- **Has PII been removed?**
  - Use [Clouseau](https://github.com/virtix/clouseau) for scanning source code.
    - For an Open Source Release, attach the Clouseau output.
  - If there are images, visually inspect each image to ensure there is no CFPB-specific information.

- **Have security vulnerabilities been remediated?**
  - Use the [OWASP Top 10](https://www.owasp.org/index.php/Top_10_2013)
  - [National Vulnerability Database](http://nvd.nist.gov/)
  - [SANS Swat Checklist](http://www.securingthehuman.org/developer/swat)

- **Are we including any other open source products? If so, is there any conflict with our public domain release?**

- **Is our `TERMS.md` included?**

- **Is a `CHANGELOG.md` present and does it contain structured, consistently formatted recent history?**
  - See <https://github.com/cfpb/qu> and <https://github.com/cfpb/hmda-explorer>
  - Some Inspiration: <http://keepachangelog.com/>

- **Are instructions for contributing included (`CONTRIBUTING.md`)?**

- **Are installation instructions clearly written in the `README` _and_ tested on a clean machine?**

- **Are all dependencies described in the `README`, `requirements.txt`, and/or `buildout.cfg`?**

- **Are the API docs generated?**

- **Are there unit tests?**

- **If appplicable and possible, is it set up in TravisCI?**

- **Have multiple people reviewed the code?**

- **Is there a screenshot in the `README`, if applicable?**


## Copy this version to paste into a GitHub issue with live checkboxes:
