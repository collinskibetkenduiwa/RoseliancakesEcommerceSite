# Testing
.Flake8
.radon
.pytest
.Server metrics
.Database metrics
.Abnormal testing
.Security testing
.unittest
.acceptance test
-use your own added setting sub file and add import it to the main file.The said file should 
be configured to run you own test runner of choice 
-code coverage should be at least 30% and the developer who has made the changes should make sure that code coverage should be a least 120% later on 
   # front end
   .browser compatibility
   .SEO
   .browser acceleration 
   .browser load time

# Versioning
We use gitlab to version the roselianCakes  platform
We use the following branches
     1.Master-code in master is code in server
     2.Developer-code has the latest bug fixes and features.It is the only one which 
       merges to master.
     3.FixBug-For fixing normal bugs and code should be updated to developers branch
     4.FixBugCritical-Fixes critical Bugs and can only merge to master without any 
         unnecessary test and documentation but prone for same later on
     5.Feature Branch -This is used for major released and related dependencies
       like license,documentation and support  
Any changes should be in its branch with appropriate name and commit message.
All merges must be reviewed by peers and commented

# Automating
     1.Use pre-commit when writing test to make sure they will run remotely to
     prevent wastage of builds
     2.Tox is used for running local tests
     3.gitlabci -is used for running and building test in repo
# Documenting
.Use sphinx tool to generate docs please find its documentation online 
.Use doc provided by django docs for debugging
# Fixing Bugs
   # critical
   .should be fixed and tested as soon as possible merged to server and updated
   # non-critical
   .should follow normal code process and documented include how it was fixed in case a
   similar problem should arise
# code quality.
 # back-end
   .flake8
   .radon
 # front-end 
   .No inline or within file css
   .No unclosed tags
