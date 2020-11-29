-- CI/CD on AWS --
    - CodePipeline - EC2 instance from CloudFormation:
        a. Create HTTP git credentials in IAM.
        b. Clone the git repo.
            # If on Windows, it'll ask credentials created above.
        c. Create git flow.
            # One time setup:
            CMD> wget -q -O - --no-check-certificate https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | bash
            CMD> export INSTALL_PREFIX=$USERPROFILE/bin
            
            # Use following to initialize the git flow.
            CMD> git flow init
        d. Create CF template.
        e. git add .
        f. git commit -m "message"
        g. git push origin develop
        h. git checkout master
        i. git merge develop
        k. git commit -m "message"
        l. git push origin "master"
        m. Create Pipeline.
        n. Skip CodeBuild.
        o. CodeDeploy > CloudFormation
    
    - CodePipeline - Lambda function with dependencies from CloudFormation:
        a. Create repo.
        b. Above steps.
	c. Follow the images...

    - NOTE:
        a. Output of one stage is the input of the next.