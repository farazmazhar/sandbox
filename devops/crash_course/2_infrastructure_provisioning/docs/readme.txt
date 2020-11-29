-- UNDERSTANDING INFRASTRUCTURE AS CODE --
    - Two ways of creating:
        a. Manual creation. (Using console, and commands etc)
        b. Automation. (Anible, Cloudformation)
    
    - Industry is moving towards IAS to reduce manual work.

    - Advantages:
        a. Reusability of code.
        b. Managing infrastructure via source control.
        c. Enable collaboration.
    
    - Use-case - deploy a HA LAMP stack:
        a. Application load balancer. (listeners + target groups)
        b. Auto-scaling. (Launch configuration + auto-scaling groups)
        c. User data scripts to install Apache, PHP.
        d. RDS DB with multi-AZ.
        e. Apt security groups.
    
    - Cloudformation workflow:
        a. Create a template.
        b. Create a stack and use the above template.
        c. Configure stack.
        d. Deploy stack.

-- IMPLEMENTING CLOUDFORMATION --
    - Ways of writing a cf template:
        a. JSON.
        b. YAML.
    
    - Writing a template (JSON):
        a. check 's3.json'.
        b. Refer following link for 'AWS Resource and Property Type Reference'.
            # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html
        
    - Configuration parameters:
        a. delete-stack
            # Deletes all the resources created from the given stack.
            # Deletion policies:
                1. Default.
                2. Retain.
                3. Snapshot.
        b. update-stack
            # Updates resources with new template created from the given stack.
    
    - Intrinsic functions:
        a. Fn::FindInMap
        b. Fn::GetAtt
        c. Fn::GetAZs // Returns list of AZs of specified region.
        d. Fn::Base64 // Encodes data into Base64.
        e. Fn::Join
    
    - Condition functions:
        a. Fn::And 
        b. Fn::Equals
        c. Fn::If 
        d. Fn::Not 
        e. Fn::Or
    
    - Parameters:
        a. Allows taking input from user.
        b. Introducing flexibilty.
        c. Usage:
            # "Parameter": { }
    
    - Nested templates:
        a. A template with-in a template.
        b. When creating a large number of stack, instead of writing separate template for each stack,
        simply write template for common components and then put remaining components in nested stack for each specific stack.

    - Wait condition:
        a. Used to wait for certain condition to be fulfilled before progressing forward.
        b. Attributes:
            # DependsOn // drawback: focuses on creation but not readiness.
        c. Signal:
            # Manual: /opt/aws/bin/cfn-signal --success true --stack STACK-NAME --resource RESOURCE-NAME --region us-east-1

    - CLI command to run YAML script.
        a. Check 'scripts\mine\0_readme.txt'