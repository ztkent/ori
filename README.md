# Ori
Manage notifications and reminders for Microsoft Teams with [BlinkStick](https://www.blinkstick.com)

## Setup
- Assuming you belong to an organization that uses Microsoft, and you are not the admin, this project connects to the Graph API with 'Delegated' permissions.  
- This means that we will only be able to read and write the authenticated user's data, not the entire organizations.  
- Hopefully, this will make it easier to get the necessary permissions from your organization's admin.  

### Create an Application Connection via Microsoft Graph API
#### Register an application in Azure Active Directory  
- Go to the Azure portal, then to Azure Active Directory, then to App registrations, and click on New registration.
- Enter a name for the application, select the supported account types, and then click Register.
- After the app is registered, note down the Application (client) ID and the Directory (tenant) ID.

#### Set API permissions
- In the App registrations page, go to API permissions, and click on "Add a Permission".
- Select Microsoft Graph, then Delegated permissions, and then add the necessary permissions.
    - `User.Read`

#### Set a Redirect URI
- In the App registrations page, go to Authentication, and click on "Add a platform".
- Choose "Mobile and desktop applications", and then select the "https://login.microsoftonline.com/common/oauth2/nativeclient" redirect URI.
- Your organization may require a different redirect URI. Enter it now.

### Configure your ENV variables
- Create a .env file in the same directory as this module, or export the following environment variables:
    ```bash
    CLIENT_ID=
    TENANT_ID=
    REDIRECT_URI=https://login.microsoftonline.com/common/oauth2/nativeclient
    ```

### Authorize the application
- When creating a new connection, your application will connect via the [Microsoft Graph Python SDK](https://github.com/microsoftgraph/msgraph-sdk-python).
- Authenicate with OAuth by logging into your Microsoft account and granting the necessary permissions.
- After successful login, a client connection is generated from the response.
- This client connection is used for all future requests.