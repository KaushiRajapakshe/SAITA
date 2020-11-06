# Variable for
# PRE SELECTED APPLICATION PROBLEM
# SOLVING SYSTEM
log_enable_all = True
log_enable_error = True
log_enable_warning = True
error_str_size = 100
logo_div = 0.3
title_bar_bg = "#3a3a3a"
window_bg = "#ffffff"
close_but_acc_bg = "#B10202"
mini_but_acc_bg = "#6F6F6F"
title_bar_but_txt_color = "#ffffff"
title_bar_txt = "SAITA - Fix Installed Application Related Issues"
title_bar_txt_color = "#ffffff"
full_window_color = "#ffffff"
head_window_color = "#ffffff"
body_window_color = "#ffffff"
message_body_color = "#ffffff"
toggle_button_enable_fg_color = "#000000"
toggle_button_enable_bg_color = "#ccc"
toggle_button_disable_bg_color = "#269900"
cell_bg = "#3a3a3a"
cell_topic_txt_color = "#ffffff"
coll_count = 4
soft_img_dev = 1.2
soft_title_f_size_dev = 45
soft_ver_f_size_dev = 30
pad_val = 20
main_search_color_bg = "#ffffff"
main_search_width = 50
main_search_color_txt = "black"
main_search_color_txt_hint = "#C1C0C0"
main_search_but_bg = "#3a3a3a"
main_search_but_hover = "#4C4C4C"
main_search_but_acc = "#504646"
main_search_but_txt_color = "#ffffff"
main_search_but_txt = "Search"
main_search_but_ipadx = 40
main_search_but_ipady = 11
loader_icon = "icon/loader.gif"
say_voice = 1
say_speed = 0.7

# Apache Jena Fuseki Server URL
url = 'http://localhost:3030/saita'

# Sample script file name
script_file = "C:\\Projects\\meerun.ps1"
script1 = "set-executionpolicy remotesigned\n$port = 80\nStop-Process -id (Get-NetTCPConnection -LocalPort $port).OwningProcess"
script2 = "set-executionpolicy remotesigned\ntaskkill /IM xampp-control.exe /F"
script3 = "taskkill /IM Code.exe /F\nStart-Sleep -s -15\nStart-Process -FilePath \"C:\\Users\\TechNoobToPro\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\""

# Ignore SAITA log path
ignore_log_path = 'IT16178700\\\\data\\\\foi.log'

# Dev variable
app_config_path = "../../app.ini"
file_in = "../icon/SAITA.png"
log_file = "../data/foi.log"
logo = "../icon/logo.ico"
log_match = "../textfile/logMatch.txt"
log_extension = "../textfile/logExtension.txt"
log_no_extension = "../textfile/logNoExtension.txt"
ontology_path = "../../ontology/saita.owl"
scanner_config_path = "../app.ini"

# Prod variable
# log_file = "data/foi.log"
# logo = "icon/logo.ico"
# log_match = "textfile/logMatch.txt"
# file_in = "icon/SAITA.png"
# log_extension = "textfile/logExtension.txt"
# log_no_extension = "textfile/logNoExtension.txt"
# app_config_path = "app.ini"
# ontology_path = "ontology/saita.owl"

# MAC VM
label2_x = 80
label4_x = 250
label4_y = 700
label5_x = 120
label5_y = 810
label3_h = 80
label3_w = 1
label3_padx = 170
label3_pady = 0
label4_xx = 890
label4_yy = 46
scrollbar_x = 1650
scrollbar_y = 110
scrollbar_h = 630
chat_log_x = 890
chat_log_y = 110
chat_log_h = 630
chat_log_w = 700
entry_box_x = 890
entry_box_y = 800
entry_box_h = 45
entry_box_w = 570
send_button_x = 1480
send_button_y = 800
send_button_h = 45

# Windows VM
# label2_x = 80
# label4_x = 230
# label4_y = 550
# label5_x = 90
# label5_y = 640
# label3_h = 50
# label3_w = 1
# label3_padx = 100
# label3_pady = 0
# label4_xx = 787
# label4_yy = 46
# scrollbar_x = 1500
# scrollbar_y = 90
# scrollbar_h = 600
# chat_log_x = 790
# chat_log_y = 90
# chat_log_h = 600
# chat_log_w = 700
# entry_box_x = 790
# entry_box_y = 700
# entry_box_h = 45
# entry_box_w = 570
# send_button_x = 1380
# send_button_y = 700
# send_button_h = 45

# Text to Speech
q1 = 'Sorry.. We missed it. Please try out for other.'
q2 = 'Please enter your application name.?'
q3 = 'Please enter your application version.?'
q4 = 'Please enter your error description.?'
q5 = 'Please wait until error analyzing.'
q6 = 'Do you need to continue.? (Yes/No)'
q7 = 'Your problem is solved. Do you have any other problem? (Yes/No)'
q8 = 'System has no issue to find. Do you have any other problem? (Yes/No)'
q9 = 'Do you have any other problem? (Yes/No)'
q10 = 'Preventing scanner will take few minutes. Do you want to continue... (Yes/No)'
q11 = 'Hi!!! This is SAITA pre selected application problem solving system.Do you like to run error preventing scan ' \
      'for your operating system.? (Yes / No)'
q12 = 'Please enter valid port for analyze the error.'
q13 = 'Please enter the scanner issue number to solve.'
q14 = "No issues to find."
q15 = " is not installed in your operating system. Please try out for other application."
