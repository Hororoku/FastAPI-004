# TS-TEST004






#あなたはWebアプリ開発者です。
Azure App Services で構築する Web API のソースコードセットを作成してください。

#条件
・使用する環境は FastAPI、Python、Pythonバージョンは3.13
・Dockerを使用し、dockerfile、requirements.txt、pyproject.tom、main.py を生成してください。
・サービスは「/」、「/help」を用意してください。 リターン値は json 形式でそれぞれ固有な値を返してください。



Quick setup — if you’ve done this kind of thing before
or	

https://github.com/Hororoku/FastAPI-004.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

create a new repository on the command line
echo "# FastAPI-004" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hororoku/FastAPI-004.git
git push -u origin main

push an existing repository from the command line
git remote add origin https://github.com/Hororoku/FastAPI-004.git
git branch -M main
git push -u origin main






GitHub Actions（CI/CD）
Azure App Service for Containers に自動デプロイする YAML**

以下は Azure Web App for Containers にデプロイする標準構成。
GitHub Secrets に以下を登録しておく必要がある：

| Secret 名                             | 内容                                                |
| ---                                   | ---                                                 |
| ``AZURE_WEBAPP_NAME``                 | App Service 名                                      |
| ``AZURE_WEBAPP_PUBLISH_PROFILE``      | App Service の Publish Profile XML                  |
| ``AZURE_CONTAINER_REGISTRY``          | ACR のログインサーバー名（例: myregistry.azurecr.io） |
| ``AZURE_CONTAINER_REGISTRY_USERNAME`` | ACR ユーザー名                                       |
| ``AZURE_CONTAINER_REGISTRY_PASSWORD`` | ACR パスワード                                       |












概要
{
    "id": "/subscriptions/113695ac-04a5-4fd5-930e-d3bf95c610e7/resourceGroups/ts-test005_group/providers/Microsoft.Web/sites/FastAPI005",
    "name": "FastAPI005",
    "type": "Microsoft.Web/sites",
    "kind": "app,linux",
    "location": "Japan West",
    "tags": {},
    "properties": {
        "name": "FastAPI005",
        "state": "Running",
        "hostNames": [
            "fastapi005-b8b7a5agcbhna8eb.japanwest-01.azurewebsites.net"
        ],
        "webSpace": "FastAPI-JapanWestwebspace-Linux",
        "selfLink": "https://waws-prod-os1-031.api.azurewebsites.windows.net:455/subscriptions/113695ac-04a5-4fd5-930e-d3bf95c610e7/webspaces/FastAPI-JapanWestwebspace-Linux/sites/FastAPI005",
        "repositorySiteName": "FastAPI005",
        "owner": null,
        "usageState": "Normal",
        "enabled": true,
        "adminEnabled": true,
        "siteScopedCertificatesEnabled": false,
        "afdEnabled": false,
        "enabledHostNames": [
            "fastapi005-b8b7a5agcbhna8eb.japanwest-01.azurewebsites.net",
            "fastapi005-b8b7a5agcbhna8eb.scm.japanwest-01.azurewebsites.net"
        ],
        "siteProperties": {
            "metadata": null,
            "properties": [
                {
                    "name": "LinuxFxVersion",
                    "value": "PYTHON|3.13"
                },
                {
                    "name": "WindowsFxVersion",
                    "value": null
                }
            ],
            "appSettings": null
        },
        "availabilityState": "Normal",
        "sslCertificates": null,
        "csrs": [],
        "cers": null,
        "siteMode": null,
        "hostNameSslStates": [
            {
                "name": "fastapi005-b8b7a5agcbhna8eb.japanwest-01.azurewebsites.net",
                "sslState": "Disabled",
                "ipBasedSslResult": null,
                "virtualIP": null,
                "virtualIPv6": null,
                "thumbprint": null,
                "certificateResourceId": null,
                "toUpdate": null,
                "toUpdateIpBasedSsl": null,
                "ipBasedSslState": "NotConfigured",
                "hostType": "Standard"
            },
            {
                "name": "fastapi005-b8b7a5agcbhna8eb.scm.japanwest-01.azurewebsites.net",
                "sslState": "Disabled",
                "ipBasedSslResult": null,
                "virtualIP": null,
                "virtualIPv6": null,
                "thumbprint": null,
                "certificateResourceId": null,
                "toUpdate": null,
                "toUpdateIpBasedSsl": null,
                "ipBasedSslState": "NotConfigured",
                "hostType": "Repository"
            }
        ],
        "hostNamePrivateStates": [],
        "computeMode": null,
        "serverFarm": null,
        "serverFarmId": "/subscriptions/113695ac-04a5-4fd5-930e-d3bf95c610e7/resourceGroups/FastAPI/providers/Microsoft.Web/serverfarms/plan-FastAPI-004",
        "reserved": true,
        "isXenon": false,
        "hyperV": false,
        "sandboxType": null,
        "lastModifiedTimeUtc": "2026-09-18T03:11:54.95",
        "storageRecoveryDefaultState": "Running",
        "contentAvailabilityState": "Normal",
        "runtimeAvailabilityState": "Normal",
        "dnsConfiguration": {},
        "containerAllocationSubnet": null,
        "useContainerLocalhostBindings": null,
        "outboundVnetRouting": {
            "allTraffic": false,
            "applicationTraffic": false,
            "contentShareTraffic": false,
            "imagePullTraffic": false,
            "backupRestoreTraffic": false,
            "managedIdentityTraffic": false
        },
        "legacyServiceEndpointTrafficEvaluation": null,
        "siteConfig": {
            "numberOfWorkers": 1,
            "defaultDocuments": null,
            "netFrameworkVersion": null,
            "phpVersion": null,
            "pythonVersion": null,
            "nodeVersion": null,
            "powerShellVersion": null,
            "linuxFxVersion": "PYTHON|3.13",
            "windowsFxVersion": null,
            "sandboxType": null,
            "windowsConfiguredStacks": null,
            "requestTracingEnabled": null,
            "remoteDebuggingEnabled": null,
            "remoteDebuggingVersion": null,
            "httpLoggingEnabled": null,
            "azureMonitorLogCategories": null,
            "acrUseManagedIdentityCreds": false,
            "acrUserManagedIdentityID": null,
            "logsDirectorySizeLimit": null,
            "detailedErrorLoggingEnabled": null,
            "publishingUsername": null,
            "publishingPassword": null,
            "appSettings": null,
            "metadata": null,
            "connectionStrings": null,
            "machineKey": null,
            "handlerMappings": null,
            "documentRoot": null,
            "scmType": null,
            "use32BitWorkerProcess": null,
            "webSocketsEnabled": null,
            "alwaysOn": false,
            "javaVersion": null,
            "javaContainer": null,
            "javaContainerVersion": null,
            "appCommandLine": null,
            "managedPipelineMode": null,
            "virtualApplications": null,
            "winAuthAdminState": null,
            "winAuthTenantState": null,
            "customAppPoolIdentityAdminState": null,
            "customAppPoolIdentityTenantState": null,
            "runtimeADUser": null,
            "runtimeADUserPassword": null,
            "loadBalancing": null,
            "routingRules": null,
            "experiments": null,
            "limits": null,
            "autoHealEnabled": null,
            "autoHealRules": null,
            "tracingOptions": null,
            "vnetName": null,
            "vnetRouteAllEnabled": null,
            "vnetPrivatePortsCount": null,
            "publicNetworkAccess": null,
            "cors": null,
            "push": null,
            "apiDefinition": null,
            "apiManagementConfig": null,
            "autoSwapSlotName": null,
            "localMySqlEnabled": null,
            "managedServiceIdentityId": null,
            "xManagedServiceIdentityId": null,
            "keyVaultReferenceIdentity": null,
            "ipSecurityRestrictions": null,
            "ipSecurityRestrictionsDefaultAction": null,
            "scmIpSecurityRestrictions": null,
            "scmIpSecurityRestrictionsDefaultAction": null,
            "scmIpSecurityRestrictionsUseMain": null,
            "http20Enabled": false,
            "minTlsVersion": null,
            "minTlsCipherSuite": null,
            "scmMinTlsCipherSuite": null,
            "supportedTlsCipherSuites": null,
            "scmSupportedTlsCipherSuites": null,
            "scmMinTlsVersion": null,
            "ftpsState": null,
            "preWarmedInstanceCount": null,
            "functionAppScaleLimit": 0,
            "elasticWebAppScaleLimit": null,
            "healthCheckPath": null,
            "fileChangeAuditEnabled": null,
            "functionsRuntimeScaleMonitoringEnabled": null,
            "websiteTimeZone": null,
            "minimumElasticInstanceCount": 0,
            "azureStorageAccounts": null,
            "http20ProxyFlag": null,
            "sitePort": null,
            "antivirusScanEnabled": null,
            "storageType": null,
            "sitePrivateLinkHostEnabled": null,
            "clusteringEnabled": false,
            "webJobsEnabled": false
        },
        "functionAppConfig": null,
        "daprConfig": null,
        "aiIntegration": null,
        "deploymentId": "FastAPI005",
        "slotName": null,
        "trafficManagerHostNames": null,
        "sku": "Free",
        "scmSiteAlsoStopped": false,
        "targetSwapSlot": null,
        "hostingEnvironment": null,
        "hostingEnvironmentProfile": null,
        "clientAffinityEnabled": false,
        "clientAffinityProxyEnabled": false,
        "useQueryStringAffinity": false,
        "blockPathTraversal": false,
        "jA4Forwarding": false,
        "clientCertEnabled": false,
        "clientCertMode": "Required",
        "clientCertExclusionPaths": null,
        "clientCertExclusionEndPoints": null,
        "hostNamesDisabled": false,
        "ipMode": "IPv4",
        "platformReleaseChannel": "Standard",
        "domainVerificationIdentifiers": null,
        "customDomainVerificationId": "836FD2BB189D3778C26352DC201C68349C877E6DF20CD2A0B5F39B0A3349AC7A",
        "kind": "app,linux",
        "managedEnvironmentId": null,
        "workloadProfileName": null,
        "resourceConfig": null,
        "inboundIpAddress": "40.74.100.138",
        "possibleInboundIpAddresses": "40.74.100.138,20.189.195.2",
        "inboundIpv6Address": "2603:1040:606:402::a3",
        "possibleInboundIpv6Addresses": "2603:1040:606:402::a3",
        "ftpUsername": "FastAPI005\\$FastAPI005",
        "ftpsHostName": "ftps://waws-prod-os1-031.ftp.azurewebsites.windows.net/site/wwwroot",
        "outboundIpAddresses": "20.210.141.205,20.210.139.103,20.210.169.195,20.210.136.75,20.210.138.244,20.210.140.203,20.78.154.251,20.78.155.2,20.78.155.5,20.78.155.21,20.78.155.33,20.78.155.42,40.74.100.138",
        "possibleOutboundIpAddresses": "20.210.141.205,20.210.139.103,20.210.169.195,20.210.136.75,20.210.138.244,20.210.140.203,20.78.154.251,20.78.155.2,20.78.155.5,20.78.155.21,20.78.155.33,20.78.155.42,20.78.155.30,20.78.155.34,20.78.155.41,20.78.155.18,20.78.155.50,20.78.155.65,20.78.155.70,20.78.155.75,20.78.155.83,20.78.155.85,20.78.155.98,20.78.155.107,20.78.155.116,20.78.155.90,20.78.155.102,20.78.155.104,20.78.155.119,20.78.155.122,40.74.100.138",
        "outboundIpv6Addresses": "2603:1040:603:7::100,2603:1040:603:15::8d,2603:1040:603:15::8e,2603:1040:603:3::ad,2603:1040:603:18::aa,2603:1040:603:3::ae,2603:1040:603:15::81,2603:1040:603:3::67,2603:1040:603:3::a5,2603:1040:603:3::a6,2603:1040:603:18::9d,2603:1040:603:3::a7,2603:1040:606:402::a3,2603:10e1:100:2::284a:648a,2603:1040:606:2::40e,2603:10e1:100:2::14bd:c302",
        "possibleOutboundIpv6Addresses": "2603:1040:603:7::100,2603:1040:603:15::8d,2603:1040:603:15::8e,2603:1040:603:3::ad,2603:1040:603:18::aa,2603:1040:603:3::ae,2603:1040:603:15::81,2603:1040:603:3::67,2603:1040:603:3::a5,2603:1040:603:3::a6,2603:1040:603:18::9d,2603:1040:603:3::a7,2603:1040:603:15::82,2603:1040:603:5::aa,2603:1040:603:18::9e,2603:1040:603:18::9f,2603:1040:603:3::a8,2603:1040:603:15::83,2603:1040:603:17::a5,2603:1040:603:5::ac,2603:1040:603:17::a6,2603:1040:603:18::a1,2603:1040:603:15::86,2603:1040:603:18::a2,2603:1040:603:18::a5,2603:1040:603:18::a6,2603:1040:603:18::a7,2603:1040:603:15::8c,2603:1040:603:3::ab,2603:1040:603:7::ff,2603:1040:606:402::a3,2603:10e1:100:2::284a:648a,2603:1040:606:2::40e,2603:10e1:100:2::14bd:c302",
        "containerSize": 0,
        "dailyMemoryTimeQuota": 0,
        "suspendedTill": null,
        "siteDisabledReason": 0,
        "functionExecutionUnitsCache": null,
        "maxNumberOfWorkers": null,
        "homeStamp": "waws-prod-os1-031",
        "cloningInfo": null,
        "hostingEnvironmentId": null,
        "tags": {},
        "resourceGroup": "ts-test005_group",
        "defaultHostName": "fastapi005-b8b7a5agcbhna8eb.japanwest-01.azurewebsites.net",
        "slotSwapStatus": null,
        "httpsOnly": true,
        "endToEndEncryptionEnabled": false,
        "functionsRuntimeAdminIsolationEnabled": false,
        "redundancyMode": "None",
        "inProgressOperationId": null,
        "geoDistributions": null,
        "privateEndpointConnections": [],
        "publicNetworkAccess": "Enabled",
        "buildVersion": null,
        "targetBuildVersion": null,
        "migrationState": null,
        "eligibleLogCategories": "AppServiceAppLogs,AppServiceConsoleLogs,AppServiceHTTPLogs,AppServicePlatformLogs,ScanLogs,AppServiceAuthenticationLogs,AppServiceAuditLogs,AppServiceIPSecAuditLogs",
        "inFlightFeatures": [
            "SiteContainers"
        ],
        "platformVersion": "110.0.7.48",
        "storageAccountRequired": false,
        "virtualNetworkSubnetId": null,
        "keyVaultReferenceIdentity": "SystemAssigned",
        "autoGeneratedDomainNameLabelScope": "TenantReuse",
        "privateLinkIdentifiers": null,
        "sshEnabled": null,
        "maintenanceEnabled": false
    }
}



デプロイログ

Running oryx build...

Command: oryx build /home/site/repository -o /home/site/wwwroot --platform python --platform-version 3.13 -p virtualenv_name=antenv --log-file /tmp/build-debug.log  -i /tmp/8df153118f0c21a --compress-destination-dir | tee /tmp/oryx-build.log
Operation performed by Microsoft Oryx, https://github.com/Microsoft/Oryx
You can report issues at https://github.com/Microsoft/Oryx/issues

Oryx Version: 0.2.20260728.2+203b718c5847f8ff2fa0f9aaeb1987e6b1bd30d7, Commit: 203b718c5847f8ff2fa0f9aaeb1987e6b1bd30d7, ReleaseTagName: 20260728.2

Build Operation ID: 8f7fbd7835dd8934
Repository Commit : b56f589f8a3928959e7f8792eea5b207afff8afa
OS Type           : bookworm
Image Type        : githubactions

Primary SDK Storage URL: https://oryx-cdn.microsoft.io
Backup SDK Storage URL: 
ACR SDK Registry URL: (not set)
SDK provider status:
  External ACR SDK provider: Enabled
  External SDK provider: Enabled
  Direct ACR SDK provider: Disabled
  Blob SDK provider: Enabled
External ACR SDK provider is enabled. Only using user-specified platform: python
Detecting platforms...
External ACR provider resolved version '3.13.14' for python.
Version resolved using external ACR SDK provider.
Detected following platforms:
  python: 3.13.14
Requesting SDK from ACR via external provider: python 3.13.14 (bookworm)
Successfully pulled SDK from ACR via external provider: python 3.13.14
SDK for 'python' version '3.13.14' fetched via external ACR provider.
Version '3.13.14' of platform 'python' is not installed. Generating script to install it...

Using intermediate directory '/tmp/8df153118f0c21a'.

Copying files to the intermediate directory...
Copying files to intermediate directory done in 0 sec(s).

Source directory     : /tmp/8df153118f0c21a
Destination directory: /home/site/wwwroot

Installing platform...

Downloading and extracting 'python' version '3.13.14' to '/tmp/oryx/platforms/python/3.13.14'...
Detected image debian flavor: bookworm.
SDK binary download was skipped. Looking for cached tarball...
Found tarball at /var/OryxAcrSdks/python/python-bookworm-3.13.14.tar.gz
Successfully extracted python version 3.13.14 from cached tarball.

Platform installation done in 7 sec(s).
Running build script snippets...
Python Version: /tmp/oryx/platforms/python/3.13.14/bin/python3.13
Creating directory for command manifest file if it does not exist
Removing existing manifest file
Python Virtual Environment: antenv
Creating virtual environment...
Executing: /tmp/oryx/platforms/python/3.13.14/bin/python3.13 -m venv antenv --copies --system-site-packages
Activating virtual environment...
Fast build is enabled
Installing uv...
Collecting uv
  Downloading uv-0.12.16-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Downloading uv-0.12.16-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (20.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.3/20.3 MB 19.2 MB/s  0:00:01
Installing collected packages: uv
Successfully installed uv-0.12.16

[notice] A new release of pip is available: 26.1.2 -> 26.2.1
[notice] To update, run: pip install --upgrade pip
Running uv pip install...
Using Python 3.13.14 environment at: antenv
Resolved 18 packages in 963ms
Downloading pydantic-core (2.0MiB)
Downloading uvloop (4.2MiB)
 Downloaded pydantic-core
 Downloaded uvloop
Prepared 18 packages in 376ms
Installed 18 packages in 181ms
Bytecode compiled 410 files in 2.74s
 + annotated-types==0.8.0
 + anyio==4.15.1
 + click==8.5.0
 + fastapi==0.115.0
 + h11==0.16.0
 + httptools==0.8.0
 + idna==3.20
 + pydantic==2.13.5
 + pydantic-core==2.46.5
 + python-dotenv==1.2.3
 + pyyaml==6.0.3
 + starlette==0.38.6
 + typing-extensions==4.16.0
 + typing-inspection==0.4.4
 + uvicorn==0.32.0
 + uvloop==0.22.1
 + watchfiles==1.2.0
 + websockets==17.1
uv pip install done in 10 sec(s).
Not a vso image, so not writing build commands

Copying 'requirements.txt' to destination directory...
Done copying requirements.txt to destination directory.
Build script snippets done in 17 sec(s).
Preparing output...
Compressing source directory directly to destination (optimized path)...
Using zstd for compression
Copied the compressed output to '/home/site/wwwroot'
Direct compression with zstd done in 6 sec(s).

Removing existing manifest file
Creating a manifest file...
Manifest file created.
Generating .ostype from DEBIAN_FLAVOR environment variable.

Total execution done in 30 sec(s).

