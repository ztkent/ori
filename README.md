# Ori
Manage notifications and reminders for Microsoft Teams with [BlinkStick](https://www.blinkstick.com)

## Setup
### Create a Teams Connection via Microsoft Graph API
#### Register an application in Azure Active Directory  
- Go to the Azure portal, then to Azure Active Directory, then to App registrations, and click on New registration.
- Enter a name for the application, select the supported account types, and then click Register.
- After the app is registered, note down the Application (client) ID and the Directory (tenant) ID.

#### Create a client secret  
- In the same App registrations page, go to Certificates & secrets, and click on New client secret.
- Enter a description for the secret, select an expiry period, and then click Add.
- After the secret is created, note down the value of the Client Secret.

#### Set API permissions
- In the App registrations page, go to API permissions, and click on "Add a Permission".
- Select Microsoft Graph, then Application permissions, and then add the necessary permissions.
    - `User.Read.All`

#### Confirm your User Prinicpal Name
- Typically, the "User Principal Name" is the email address of the user you have configured for the application.
- To confirm, go to the Azure portal, then to Users. You should see the user for the application.

### Configure your ENV variables
- Create a .env file in the same directory as the script, or export the following environment variables:
    ```bash
    CLIENT_ID=
    CLIENT_SECRET=
    TENANT_ID=
    USER_PRINCIPAL_NAME=
    ```