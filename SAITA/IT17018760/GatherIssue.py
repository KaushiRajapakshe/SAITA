import sys

from ExecuteScripts import Exe
from Powershell.StartSubService import StartSubser
from Powershell.CreateService import CreateService
from Powershell.DeleteService import DeleteServiceClass
from Powershell.Start import StartServiceClass
from Powershell.Stop import StopServiceClass
from Powershell.StartupType import StartTypeChangeClass
from Powershell.DiscriptionChange import DiscriptionChangeClass
from Powershell.DisplayNameChange import DisplayNameChangeClass

dependant_service=['wampmysqld64','EventSystem','AdobeUpdateService','AGMService','AGSService','AJRouter','ALG','AppHostSvc','AppIDSvc','Appinfo','AppMgmt','AppReadiness','AppVClient','AppXSvc','ArmouryLiveUpdate','AsHidService','ASLDRService','aspnet_state','AssignedAccessManagerSvc','asus','ASUSHookService','asusm','AudioEndpointBuilder','Audiosrv','autotimesvc','AVP20.0','AxInstSV','BcastDVRUserService_35e41f7','BDESVC','BFE','BITS','BluetoothUserService_35e41f7','BrokerInfrastructure','Browser','BTAGService','BthAvctpSvc','bthserv','camsvc','CaptureService_35e41f7','cbdhsvc_35e41f7','CDPSvc','CDPUserSvc_35e41f7','CertPropSvc','ClickToRunSvc','ClipSVC','COMSysApp','ConsentUxUserSvc_35e41f7','CoreMessagingRegistrar','cphs','cplspcon','CredentialEnrollmentManagerUserSvc_35e41f7','CryptSvc','CscService','DcomLaunch','defragsvc','DevActSvc','DeviceAssociationBrokerSvc_35e41f7','DeviceAssociationService','DeviceInstall','DevicePickerUserSvc_35e41f7','DevicesFlowUserSvc_35e41f7','DevQueryBroker','Dhcp','diagnosticshub.standardcollector.service','diagsvc','DiagTrack','DispBrokerDesktopSvc','DisplayEnhancementService','DmEnrollmentSvc','dmwappushservice','Dnscache','DoSvc','dot3svc','DPS','DSAService','DSAUpdateService','DsmSvc','DsSvc','DusmSvc','Eaphost','EasyAntiCheat','EFS','embeddedmode','EntAppSvc','esifsvc','ESRV_SVC_QUEENCREEK','EventLog','EventSystem','Fax','fdPHost','FDResPub','fhsvc','FontCache','FontCache3.0.0.0','FrameServer','GoogleChromeElevationService','gpsvc','GraphicsPerfSvc','gupdate','gupdatem','hidserv','HvHost','ibtsiva','icssvc','igccservice','igfxCUIService2.0.0.0','IKEEXT','InstallService','Intel(R) Capability Licensing Service TCP IP Interface','Intel(R) SUR QC SAM','Intel(R) TPM Provisioning Service','iphlpsvc','IpxlatCfgSvc','jhi_service','KeyIso','klvssbridge64_20.0','KSDE4.0','KtmRm','LanmanServer','LanmanWorkstation','lfsvc','LicenseManager','LightingService','lltdsvc','lmhosts','LMS','LSM','LxpSvc','MapsBroker','MessagingService_35e41f7','MozillaMaintenance','mpssvc','MSDTC','MSiSCSI','msiserver','MSMQ','NaturalAuthentication','NcaSvc','NcbService','NcdAutoSetup','Netlogon','Netman','NetMsmqActivator','NetPipeActivator','netprofm','NetSetupSvc','NetTcpActivator','NetTcpPortSharing','NgcCtnrSvc','NgcSvc','NlaSvc','nsi','NvContainerLocalSystem','NvContainerNetworkService','NVDisplay.ContainerLocalSystem','OneSyncSvc_35e41f7','OracleJobSchedulerXE','OracleOraDB18Home1MTSRecoveryService','OracleOraDB18Home1TNSListener','OracleServiceXE','OracleVssWriterXE','Origin Client Service','Origin Web Helper Service','ose64','p2pimsvc','p2psvc','PcaSvc','PeerDistSvc','perceptionsimulation','PerfHost','PhoneSvc','PimIndexMaintenanceSvc_35e41f7','pla','PlugPlay','PNRPAutoReg','PNRPsvc','PolicyAgent','Power','PrintNotify','PrintWorkflowUserSvc_35e41f7','ProfSvc','PSI_SVC_2','PushToInstall','QMEmulatorService','QWAVE','RasAuto','RasMan','RemoteAccess','RemoteRegistry','RetailDemo','RmSvc','ROGGamingCenterService','ROGOSDService','RpcEptMapper','RpcLocator','RpcSs','SamSs','SCardSvr','ScDeviceEnum','Schedule','SCPolicySvc','SDRSVC','seclogon','SecurityHealthService','SEMgrSvc','SENS','Sense','SensorDataService','SensorService','SensrSvc','SessionEnv','SgrmBroker','SharedAccess','SharedRealitySvc','ShellHWDetection','shpamsvc','smphost','SmsRouter','SNMPTRAP','spectrum','Spooler','sppsvc','SQLWriter','SSDPSRV','ssh-agent','sshd','SstpSvc','StateRepository','Steam Client Service','stisvc','StorSvc','svsvc','swprv','SysMain','SystemEventsBroker','SystemUsageReportSvc_QUEENCREEK','TabletInputService','TapiSrv','TermService','Themes','TieringEngineService','TimeBrokerSvc','TokenBroker','TrkWks','TroubleshootingSvc','TrustedInstaller','tzautoupdate','UevAgentService','UmRdpService','UnistoreSvc_35e41f7','upnphost','USER_ESRV_SVC_QUEENCREEK','UserDataSvc_35e41f7','UserManager','uSHAREitSvc','UsoSvc','VacSvc','VaultSvc','VBoxSDS','vds','VMAuthdService','vmicguestinterface','vmicheartbeat','vmickvpexchange','vmicrdv','vmicshutdown','vmictimesync','vmicvmsession','vmicvss','VMnetDHCP','VMUSBArbService','VMware NAT Service','VMwareHostd','VSS','VSStandardCollectorService150','W32Time','w3logsvc','W3SVC','WaaSMedicSvc','WalletService','WarpJITSvc','WAS','wbengine','WbioSrvc','Wcmsvc','wcncsvc','WdiServiceHost','WdiSystemHost','WdNisSvc','WebClient','Wecsvc','WEPHOSTSVC','wercplsupport','WerSvc','WFDSConMgrSvc','WiaRpc','WinDefend','WinHttpAutoProxySvc','Winmgmt','WinRM','wisvc','WlanSvc','wlidsvc','wlpasvc','WManSvc','wmiApSrv','WMPNetworkSvc','workfolderssvc','WpcMonSvc','WPDBusEnum','WpnService','WpnUserService_35e41f7','wscsvc','WSearch','wuauserv','WwanSvc','XblAuthManager','XblGameSave','XboxGipSvc','XboxNetApiSvc','XTU3SERVICE ','AdobeFlashPlayerUpdateSvc','AJRouter','ALG','AppIDSvc','Appinfo','AppMgmt','AppReadiness ','AppXSvc','aspnet_state ','AudioEndpointBuilder','Audiosrv','AxInstSV','BDESVC ','BFE','BITS','BrokerInfrastructure','Browser','BthHFSrv','bthserv','CDPSvc ','CertPropSvc','ClipSVC','COMSysApp','CoreMessagingRegistrar','cphs','cplspcon','CryptSvc','CscService','CxAudioSvc','CxUtilSvc','DcomLaunch','DcpSvc ','defragsvc','DeviceAssociationService','DeviceInstall','DevQueryBroker','Dhcp','diagnosticshub.standardcollector.service','DiagTrack','DmEnrollmentSvc ','dmwappushservice','Dnscache','DoSvc','dot3svc','DPS','DsmSvc ','DsSvc','Eaphost','EFS','embeddedmode ','EntAppSvc','EventLog','EventSystem','Fax','fdPHost','FDResPub','fhsvc','FontCache','FontCache3.0.0.0','fpCsEvtSvc','GoogleChromeElevationService','gpsvc','gupdate','gupdatem','gusvc','hidserv','HomeGroupProvider','hpsrv','icssvc ','IEEtwCollectorService ','igfxCUIService2.0.0.0 ','IKEEXT ','IntelAudioService','iphlpsvc','KeyIso ','KtmRm','LanmanServer ','LanmanWorkstation','lfsvc','LicenseManager','lltdsvc','lmhosts','LSM','MapsBroker','McAfee WebAdvisor','MozillaMaintenance','MpsSvc ','MSDTC','MSiSCSI','msiserver','NcaSvc ','NcbService','NcdAutoSetup ','Netlogon','Netman ','netprofm','NetSetupSvc','NetTcpPortSharing','NgcCtnrSvc','NgcSvc ','NlaSvc ','nsi','NVDisplay.ContainerLocalSystem','ose','p2pimsvc','p2psvc ','PcaSvc ','PeerDistSvc','PerfHost','pla','PlugPlay','PNRPAutoReg','PNRPsvc','PolicyAgent','Power','PrintNotify','ProfSvc','PSI_SVC_2','QWAVE','RasAuto','RasMan ','RemoteAccess ','RemoteRegistry','RetailDemo','RpcEptMapper ','RpcLocator','RpcSs','SamSs','SCardSvr','ScDeviceEnum ','Schedule','SCPolicySvc','SDRSVC ','seclogon','SENS','SensorDataService','SensorService','SensrSvc','SessionEnv','SharedAccess ','ShellHWDetection','smphost','SmsRouter','SNMPTRAP','Spooler','sppsvc ','SSDPSRV','SstpSvc','StateRepository ','stisvc ','StorSvc','svsvc','swprv','SynTPEnhService ','SysMain','SystemEventsBroker','TabletInputService','TapiSrv','TeamViewer','TermService','Themes ','tiledatamodelsvc','TimeBroker','TrkWks ','TrustedInstaller','UI0Detect','UmRdpService ','upnphost','UserManager','UsoSvc ','valWBFPolicyService','VaultSvc','VBoxSDS','vds','VMAuthdService','vmicguestinterface','vmicheartbeat','vmickvpexchange ','vmicrdv','vmicshutdown ','vmictimesync ','vmicvmsession','vmicvss','VMnetDHCP','VMUSBArbService ','VMware NAT Service','VMwareHostd','VRLService','vrswrm-service','VSS','W32Time','WalletService','wampapache64 ','wampmariadb64','wampmysqld64 ','wbengine','WbioSrvc','Wcmsvc ','wcncsvc','WcsPlugInService','WdiServiceHost','WdiSystemHost','WdNisSvc','WebClient','Wecsvc ','WEPHOSTSVC','wercplsupport','WerSvc ','WiaRpc ','WinDefend','WinHttpAutoProxySvc','Winmgmt','WinRM','WlanSvc','wlidsvc','wmiApSrv','WMPNetworkSvc','workfolderssvc','WPDBusEnum','WpnService','wscsvc ','WSearch','WSService','wuauserv','wudfsvc','WwanSvc','XblAuthManager','XblGameSave','XboxNetApiSvc','AdobeARMservice','AdobeUpdateService','AESMService','AGMService','AGSService','Appinfo','AudioEndpointBu...','Audiosrv','BFE','BITS','BrokerInfrastru...','BthAvctpSvc','camsvc','cbdhsvc_118b8c446','CDPSvc','CDPUserSvc_118b...','ClickToRunSvc','COMSysApp','CoreMessagingRe...','cphs','cplspcon','CryptSvc','DbxSvc','DcomLaunch','DDVCollectorSvcApi','DDVDataCollector','DDVRulesProcessor','DellHardwareS...','DellSupportAss...','DellClientManag...','DellDigitalDeli...','DeviceAssociati...','Dhcp','DiagTrack','DispBrokerDeskt...','DisplayEnhancem...','Dnscache','DPS','DsSvc','DusmSvc','esifsvc','EventLog','EventSystem','EvtEng','FDResPub','FontCache','FontCache3.0.0.0','hidserv','IAStorDataMgrSvc','igfxCUIService2...','IKEEXT','InstallService','Intel(R)Capabi...','iphlpsvc','jhi_service','KillerNetwork...','LanmanServer','LanmanWorkstation','lfsvc','LicenseManager','lmhosts','LMS','McAfeeWebAdvisor','McAPExe','mccspsvc','mfemms','mfevtp','MongoDB','mpssvc','MSDTC','MySQL57','NcbService','NgcCtnrSvc','NgcSvc','NlaSvc','nsi','OracleServiceXE','OracleXETNSList...','PcaSvc','PEFService','PimIndexMainten...','PlugPlay','PolicyAgent','Power','ProfSvc','QMEmulatorService','QWAVE','RegSrvc','RmSvc','RNDBWM','RpcEptMapper','RpcSs','RstMwService','RtkAudioUnivers...','SamSs','Schedule','SecurityHealthS...','SEMgrSvc','SENS','SgrmBroker','ShellHWDetection','SmartByteNetwo...','Spooler','sppsvc','SSDPSRV','SstpSvc','stisvc','StorSvc','SupportAssistAgent','SysMain','SystemEventsBroker','TabletInputService','Themes','TimeBrokerSvc','TokenBroker','TrkWks','UnistoreSvc_118...','UserDataSvc_118...','UserManager','UsoSvc','VaultSvc','WavesSysSvc','WbioSrvc','Wcmsvc','wcncsvc','WDDriveService','WdiServiceHost','WdiSystemHost','WdNisSvc','WinDefend','WinHttpAutoProx...','Winmgmt','WlanSvc','wlidsvc','WpnService','WpnUserService_...','wscsvc','WSearch','wuauserv','XblAuthManager','XboxNetApiSvc','xTendUtilitySer...','ZeroConfigService']

class TestCall(object):
    IssuedService = None
    @classmethod
    def IssueSolve(cls):
        error=input("Please explain your issue in Services : ")
        if any(word in error for word in dependant_service) or any(word in error for word in dependant_service) :
            Error_List = error.split()
            if any(word in error for word in dependant_service):
                def common(Error_List, dependant_service):
                    c = [value for value in Error_List if value in dependant_service]
                    return c
                d = common(Error_List, dependant_service)
                cls.IssuedService=(d[0])
                print(cls.IssuedService)
                print("final print")
                print(Exe().run_script(cls.IssuedService))

        else:
            print("Cannot Identify your service name or issue.Try again.")
            cls.IssueSolve()




def CreateDeleteModify():
    print("Select one of the following      1.Create Service    2.Delete Service   3.Modify Service")
    createcat=input("Enter the selected number: ")

    if createcat=="1":
        print("Answer the following questions before create service.")
        print(CreateNewService.CreateService())
    elif createcat=="2":
        print(DeleteService.DeleteAddedService())
    elif createcat=="3":
        print(ModifyService.ModifyAddedService())


class CreateNewService(object):
    @classmethod
    def CreateService(createp):

        createp.ques1=input("Enter the service name to create: ")
        createp.ques2=input("Enter the service description: ")
        createp.ques3=input("Select the startup type:     1.Manual   2.Automatic   3.Disabled    : " )

        return CreateService().createnew(createp.ques1,createp.ques2,createp.ques3)


class DeleteService(object):
    @classmethod
    def DeleteAddedService(deleteser):
        deleteser.ques4=input("Enter the service name to delete: ")
        confirmDel=input("Confirm Deletion?    1.Yes   2.No ")
        if confirmDel=="1":
            return DeleteServiceClass().deleteservice(deleteser.ques4)
        else:
            print("Thank you for join with SAITA")
            exit()


class ModifyService(object):
    @classmethod
    def ModifyAddedService(modiuser):
        print("In this function you can modify only the startup type,discription and display name.And also you can start or stop service from this function")
        modifyselect=input("Select what do you want to do?   1.Change Display Name  2.Change Discription   3.Change Start Type    4.Start   5.Stop :" )
        if modifyselect=="1":
            modiuser.stService = input("Enter the service name: ")
            modiuser.displayName = input("Enter new discription: ")
            return DisplayNameChangeClass().DisplayNameChange(modiuser.stService, modiuser.displayName)
            print("display name")
        elif modifyselect == "2":
            modiuser.stService = input("Enter the service name: ")
            modiuser.discriptionSer = input("Enter new discription: ")
            return DiscriptionChangeClass().DiscriptionChange(modiuser.stService,modiuser.discriptionSer)
        elif modifyselect=="3":
            modiuser.stService = input("Enter the service name: ")
            modiuser.stType = input("Select the startup type:     1.Manual   2.Automatic   3.Disabled : ")
            return StartTypeChangeClass().StartTypeChange(modiuser.stService,modiuser.stType)
        elif modifyselect=="4":
            modiuser.stService=input("Enter the service name: ")
            return StartServiceClass().StartService(modiuser.stService)
        elif modifyselect=="5":
            modiuser.stService=input("Enter the service name: ")
            return StopServiceClass().StopService(modiuser.stService)



print("Select Category you wish to continue:      1. Create/Delete/Modify Service      2. Issue in Currpted Service")
error1 = input("Please Enter the selected number : ")

if error1=="1":
    CreateDeleteModify()
elif error1=="2":
    TestCall.IssueSolve()









