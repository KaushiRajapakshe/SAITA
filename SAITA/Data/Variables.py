sql_server = "localhost"
sql_db = "saita"
sql_uname = "root"
sql_password = ""
log_enable_all = True
log_enable_error = True
log_enable_warning = True
img_location = "Icon/SAITA.png"
log_file = "Data/System.log"
logo = "Icon/logo.ico"
logo_div = 0.3
title_bar_bg = "#3a3a3a"
window_bg = "#ffffff"
close_but_acc_bg = "#B10202"
mini_but_acc_bg = "#6F6F6F"
title_bar_but_txt_color = "#ffffff"
title_bar_txt = "SAITA"
title_bar_txt_color = "#ffffff"
full_window_color = "#ffffff"
head_window_color = "#ffffff"
body_window_color = "#ffffff"
cell_bg = "#3a3a3a"
cell_topic_txt_color = "#ffffff"
coll_count = 4
soft_img_dev = 1.2
soft_title_f_size_dev = 45
soft_ver_f_size_dev = 30
pad_val = 20

shutdownMSG=" Add-Type -AssemblyName PresentationCore,PresentationFramework; $msgBody = ""Your Windows will restart after 30 seconds.Save your works.""; [System.Windows.MessageBox]::Show($msgBody)"
restartCode="Add-Type -AssemblyName PresentationCore,PresentationFramework;$ButtonType = [System.Windows.MessageBoxButton]::YesNo;$MessageIcon = [System.Windows.MessageBoxImage]::Error;$MessageBody = 'Do you want to continue with the restart ?';$MessageTitle = 'SAITA Alert';$Result = [System.Windows.MessageBox]::Show($MessageBody,$MessageTitle,$ButtonType,$MessageIcon);if($Result -eq 'Yes'){Restart-Computer}"
#bat_files=['..\\IT16178700\\Runner.bat','..\\IT17018760\\Runner.bat','..\\IT17056212\\Runner.bat','..\\IT17152938\\Runner.bat']
bat_files=['IT16178700\\Runner.bat','IT17018760\\Runner.bat','IT17056212\\Runner.bat','IT17152938\\Runner.bat']