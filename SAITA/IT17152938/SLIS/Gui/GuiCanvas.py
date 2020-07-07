from Gui.GuiCart import *
import time

# search box
search_box = None
# search button
search_but = None

# body
body_window = None
body_window_canves = None

# img array
soft_img_array = None

# add_button_array
add_button_array = None

# select_box_array
select_box_array = None
select_box_value_array = None

# cart_lable
cart_lable_img = None
cart_lable_txt = None
cart_img = None
cart_form = None

# scale
scale_get = None
scale = None

# coll_count
coll_count = init_coll_count;

# zoom img
zoom_in_img = None
zoom_out_img = None

time1 = None


def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = create_head_show_window(full_show_window)
    separator_window = create_separator_window_window(full_show_window)
    body_show_window = create_body_show_window(full_show_window)
    footer_show_window = create_footer_show_window(full_show_window)
    head_show_window.pack(fill=X)
    separator_window.pack(fill=X)
    body_show_window.pack(expand=1, fill=BOTH)
    footer_show_window.pack(fill=X, ipady=pad_val * acc_ra * 0.2)
    return full_show_window


def create_separator_window_window(full_window):
    return Frame(full_window, bg=separator_color, highlightthickness=0)


def create_footer_show_window(full_window):
    global scale_get, scale, zoom_in_img, zoom_out_img

    footer_window = Frame(full_window, bg=footer_window_color, highlightthickness=0)

    clock = Label(footer_window, bg=footer_window_color, font="bold", fg=clock_txt_color)
    clock.pack(padx=pad_val * acc_ra * 2, side=LEFT)

    def tick():
        global time1
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)

    clock.config(text="CLOCK:" + str(tick()))


    zoom_in_img = ImageTk.PhotoImage(create_img(img_zoom_in))
    zoomin = Label(footer_window,
                   image=zoom_in_img,
                   bg=footer_window_color,

                   )
    zoomin.pack(
        side=RIGHT,

    )

    scale_get = IntVar()
    scale = Scale(footer_window, variable=scale_get, troughcolor=title_bar_bg, from_=10, to=2, fg=main_search_color_txt,
                  orient=HORIZONTAL,
                  bg=footer_window_color)
    scale.pack(side=RIGHT)

    zoom_out_img = ImageTk.PhotoImage(create_img(img_zoom_out))
    zoomout = Label(footer_window, bg=footer_window_color, image=zoom_out_img, )

    zoomout.pack(
        side=RIGHT,

    )

    scale.bind("<ButtonRelease-1>", set_scale_col_size)
    scale.set(init_coll_count)
    return footer_window


def create_img(path):
    z_img = Image.open(path)
    n_img_w, n_img_h = z_img.size
    n_img_w *= acc_ra * zoom_dev
    n_img_h *= acc_ra * zoom_dev
    z_img = z_img.resize((round(n_img_w), round(n_img_h)))
    return z_img


def create_head_show_window(full_window):
    global search_box, search_but, cart_lable_txt, cart_lable_img, cart_form
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)
    search_box = Entry(head_window,
                       bg=main_search_color_bg,
                       fg=main_search_color_txt_hint,
                       font="bold",
                       width=round(main_search_width * acc_ra)
                       )

    search_box.pack(
        side=LEFT,
        padx=pad_val * acc_ra * 2,
        pady=pad_val * acc_ra,
        ipadx=pad_val * acc_ra,
        ipady=pad_val * acc_ra

    )
    search_box.insert(0, search_box_txt)

    search_but = Button(head_window,
                        text=main_search_but_txt,
                        bg=main_search_but_bg,
                        activebackground=main_search_but_acc,
                        bd=2,
                        font="bold",
                        fg=main_search_but_txt_color,
                        activeforeground=main_search_but_txt_color,
                        highlightthickness=0,
                        )

    search_but.pack(
        side=LEFT,
        padx=pad_val * acc_ra,
        pady=pad_val * acc_ra,
        ipadx=main_search_but_ipadx * acc_ra,
        ipady=main_search_but_ipady * acc_ra,
    )

    cart_form = Frame(head_window, bg=main_search_but_bg)
    cart_form.pack(side=RIGHT, padx=pad_val * acc_ra, pady=pad_val * acc_ra, )

    cart_lable_img = Label(cart_form, text="Version :", bg=head_window_color)
    cart_lable_img.pack(side=RIGHT, padx=2, pady=2)

    cart_lable_txt = Label(cart_form, text="", bg=main_search_but_bg, fg=cart_txt_color,
                           font="bold", )
    cart_lable_txt.pack(side=RIGHT, padx=2)

    # bind search key to event

    search_but.bind("<Button-1>", search_soft)
    cart_form.bind("<Button-1>", open_cart)
    cart_lable_img.bind("<Button-1>", open_cart)
    cart_lable_txt.bind("<Button-1>", open_cart)
    search_but.bind("<Enter>", search_button_hover_in)
    search_but.bind("<Leave>", search_button_hover_out)
    search_box.bind("<Return>", search_soft)
    search_box.bind("<KeyRelease>", search_key_enter)
    cart_form.bind("<Enter>", cart_labal_horver_in)
    cart_form.bind("<Leave>", cart_labal_horver_out)
    search_box.bind("<FocusIn>", set_plase_holder_in)
    search_box.bind("<FocusOut>", set_plase_holder_out)
    create_cart_labal()
    return head_window


def set_scale_col_size(event):
    global coll_count
    coll_count = scale_get.get()
    search_normel()


def set_plase_holder_out(event):
    global search_box
    if search_box.get() == "":
        search_box.insert(0, search_box_txt)
        search_box['fg'] = main_search_color_txt_hint


def set_plase_holder_in(event):
    global search_box
    if search_box.get() == search_box_txt:
        search_box.delete(0, "end")
        search_box['fg'] = main_search_color_txt


def create_cart_labal():
    global cart_lable_img, cart_img, cart_lable_txt
    if len(install_list) > 0:
        c_img = Image.open(img_hand_down_cart)
        cart_lable_txt['text'] = str(len(install_list))
    else:
        c_img = Image.open(img_cart)
        cart_lable_txt['text'] = ""

    c_img_w, c_img_h = c_img.size
    c_img_w *= acc_ra * cart_img_div
    c_img_h *= acc_ra * cart_img_div
    c_img = c_img.resize((round(c_img_w), round(c_img_h)))
    cart_img = ImageTk.PhotoImage(c_img)
    cart_lable_img['image'] = cart_img


def cart_labal_horver_in(event):
    global cart_lable_img, cart_img, cart_form
    if len(install_list) > 0:
        c_img = Image.open(img_hand_up_cart)
    else:
        c_img = Image.open(img_cart)

    c_img_w, c_img_h = c_img.size
    c_img_w *= acc_ra * cart_img_div
    c_img_h *= acc_ra * cart_img_div
    c_img = c_img.resize((round(c_img_w), round(c_img_h)))
    cart_img = ImageTk.PhotoImage(c_img)
    cart_lable_img['image'] = cart_img
    cart_form['bg'] = main_search_but_hover
    cart_lable_txt['bg'] = main_search_but_hover


def cart_labal_horver_out(event):
    global cart_lable_img, cart_img, cart_form
    if len(install_list) > 0:
        c_img = Image.open(img_hand_down_cart)
    else:
        c_img = Image.open(img_cart)

    c_img_w, c_img_h = c_img.size
    c_img_w *= acc_ra * cart_img_div
    c_img_h *= acc_ra * cart_img_div
    c_img = c_img.resize((round(c_img_w), round(c_img_h)))
    cart_img = ImageTk.PhotoImage(c_img)
    cart_lable_img['image'] = cart_img
    cart_form['bg'] = main_search_but_bg
    cart_lable_txt['bg'] = main_search_but_bg


def create_body_show_window(full_window):
    global body_window, body_window_canves
    main_body_window = Frame(full_window, bg=body_window_color, highlightthickness=0, padx=pad_val * acc_ra,
                             pady=pad_val * acc_ra)
    body_window_canves = Canvas(main_body_window, bg=body_window_color, highlightthickness=0)
    body_window = Frame(body_window_canves, bg=body_window_color)
    body_scrollbar = Scrollbar(main_body_window, orient="vertical", command=body_window_canves.yview)
    body_window_canves.configure(yscrollcommand=body_scrollbar.set)
    body_scrollbar.pack(side="right", fill="y")
    body_window_canves.pack(expand=1, fill=BOTH)
    body_window_canves.create_window((0, 0), window=body_window, anchor='nw')
    body_window.bind("<Configure>", scroll_all)
    main_con = MainController()
    soft_list = main_con.get_soft_list_full()
    create_body_data(soft_list, main_con.get_insalled_list())
    return main_body_window


def search_key_enter(event):
    global search_box, body_window_canves
    if search_box.get() == "":
        add_log(log_types[2], "GuiCanvas.py", "search_key_enter : " + str(event) + "  Data : Empty search bar")
        main_con = MainController()
        soft_list = main_con.get_soft_list_full()
        create_body_data(soft_list, main_con.get_insalled_list())
        body_window_canves.config(scrollregion=body_window_canves.bbox("all"))


def search_soft(event):
    global body_window_canves
    add_log(log_types[2], "GuiCanvas.py", "search_soft : " + str(event) + "  Data : " + search_box.get())
    search_normel()
    body_window_canves.yview_moveto(0.0)


def search_normel():
    global search_box, body_window_canves
    tx = search_box.get()
    if tx == search_box_txt:
        tx = ""
    main_con = MainController()
    soft_list = main_con.get_soft_list_search(tx)
    create_body_data(soft_list, main_con.get_insalled_list())


def search_button_hover_in(event):
    global search_but
    add_log(log_types[2], "GuiCanvas.py", "search_button_hover_in : " + str(event))
    search_but['bg'] = main_search_but_hover


def search_button_hover_out(event):
    global search_but
    add_log(log_types[2], "GuiCanvas.py", "search_button_hover_out : " + str(event))
    search_but['bg'] = main_search_but_bg


def scroll_all(event):
    global body_window_canves
    add_log(log_types[2], "GuiCanvas.py", "scroll_all : " + str(event))
    body_window_canves.configure(scrollregion=body_window_canves.bbox("all"))


def create_body_data(soft_list, installed_list):
    global body_window, work_area, acc_ra, soft_img_array, add_button_array, select_box_array, select_box_value_array, coll_count

    # soft_img_array = None
    soft_img_array = []
    # add_button_array = None
    add_button_array = []
    # select_box_array = None
    select_box_array = []
    select_box_value_array = []
    wid = round((work_area[2] - (round(pad_val * acc_ra) * coll_count)) / coll_count)
    soft_title_f_size = round((soft_title_f_size_dev / coll_count) / acc_ra)
    soft_ver_f_size = round((soft_ver_f_size_dev / coll_count) / acc_ra)
    add_log(log_types[2], "GuiCanvas.py", "create_body_data : " + str(soft_list))
    ch = 0
    x_range = math.ceil(len(soft_list) / coll_count)
    # x_range = 50
    # clear body window
    for widget in body_window.winfo_children():
        widget.destroy()

    for x in range(x_range):
        row_frame = Frame(body_window, bg=body_window_color, highlightthickness=0)
        for y in range(coll_count):
            if ch == len(soft_list):
                break
            else:
                singal_frame = Frame(row_frame, bg=body_window_color, highlightthickness=0, width=wid, height=wid,
                                     padx=pad_val * acc_ra, pady=pad_val * acc_ra)
                singal_frame_in = Frame(singal_frame, bg=cell_bg, width=wid, height=wid,
                                        relief='raised',
                                        bd=0)
                singal_frame.pack(side=LEFT, )
                singal_frame.pack_propagate(0)
                singal_frame_in.pack(side=LEFT, expand=True)
                singal_frame_in.pack_propagate(0)

                # soft name
                soft_topic = Label(singal_frame_in, text=soft_list[ch]['name'], bg=cell_bg, fg=cell_topic_txt_color,
                                   font="bold", pady=0)
                soft_topic.config(font=("arial", soft_title_f_size))
                soft_topic.pack(expand=True, fill='x')

                # soft image
                url_img = img_location + soft_list[ch]['img']
                soft_img = None
                try:
                    soft_img = Image.open(urlopen(url_img))
                except HTTPError as err:
                    add_log(log_types[1], "GuiCanvas.py", "Image not found in : " + url_img + " error : " + str(err))
                    soft_img = Image.open(not_found_img)
                except URLError as err:
                    add_log(log_types[0], "GuiCanvas.py", "Cant connect resources server : " + str(err))
                    soft_img = Image.open(not_found_img)

                img_frame = Frame(singal_frame_in, bg=cell_bg,
                                  relief='raised',
                                  bd=0)
                img_frame.pack(expand=True, fill=X)

                soft_img_w, soft_img_h = soft_img.size
                soft_img_w /= (coll_count * soft_img_dev)
                soft_img_h /= (coll_count * soft_img_dev)
                soft_img = soft_img.resize((round(soft_img_w), round(soft_img_h)))
                soft_img_get = ImageTk.PhotoImage(soft_img)
                soft_img_array.append(soft_img_get)
                soft_img_labal = Label(img_frame, image=soft_img_array[ch], bg=cell_bg, )
                soft_img_labal.pack(expand=True, side=LEFT)
                if 'installed' in soft_list[ch]:

                    in_show_form = Frame(img_frame, bg=installed_box_bg,
                                         relief='raised',
                                         bd=0)
                    in_show_form.pack(expand=True, side=LEFT)

                    instaled = Label(in_show_form, text='Installed :', bg=installed_box_bg, fg=cell_topic_txt_color,
                                     font="bold")
                    instaled.config(font=("arial", round(soft_title_f_size / 1.5)))
                    instaled.pack(expand=True, fill=X)

                    in_in_show_form = Frame(in_show_form, bg=installed_box_bg,
                                            relief='raised',
                                            bd=0)
                    in_in_show_form.pack(expand=True, fill=X)
                    tx = ""
                    for v in soft_list[ch]['installed_ver']:
                        # v_no_split = str(v).split('.')
                        # v_no_ok = None
                        # if len(v_no_split) > 1:
                        #     v_no_ok = v_no_split[0] + "." + v_no_split[1]
                        # else:
                        #     v_no_ok = v_no_split[0] + ".0"
                        v_no_ok = v
                        if v_no_ok is None:
                            tx += "undefined" + "\n"
                        else:
                            tx += str(v_no_ok) + "\n"

                    instaled = Label(in_in_show_form, text=tx, bg=installed_box_bg, fg=cell_topic_txt_color,
                                     font="bold", justify='right')
                    instaled.config(font=("arial", round(soft_title_f_size / 1.8)))
                    instaled.pack(side=RIGHT,
                                  padx=pad_val * acc_ra,
                                  )

                # -------------------version frame---------------------
                ver_frame = Frame(singal_frame_in, bg=cell_bg,
                                  relief='raised',
                                  bd=0)
                ver_frame.pack(expand=True, fill=X)
                # version Labal
                soft_ver_la = Label(ver_frame, text="Version :", bg=cell_bg, fg=cell_topic_txt_color,
                                    font="bold", )
                soft_ver_la.config(font=("arial", soft_ver_f_size))
                soft_ver_la.pack(expand=True, side=LEFT)

                # version Box
                soft_ver_box = create_combobox(ver_frame, soft_list[ch], installed_list)
                select_box_array.append(soft_ver_box)
                select_box_array[ch].config(font=("arial", round(soft_ver_f_size * 0.7)))
                select_box_array[ch].pack(expand=True, side=LEFT)
                select_box_array[ch].bind("<<ComboboxSelected>>",
                                          lambda eff, array_id_pass=ch, get_soft_name=soft_list[ch]['name']:
                                          select_box_change(eff, array_id=array_id_pass, soft_name=get_soft_name))

                # ----------------------------------------

                # add button

                soft_add_butt = Button(singal_frame_in,
                                       text='+',
                                       bg=soft_add_butt_bg,
                                       activebackground=soft_add_butt_acc,
                                       bd=0,
                                       font="bold",
                                       fg=soft_add_butt_txt,
                                       activeforeground=soft_add_butt_txt,
                                       highlightthickness=0
                                       )

                soft_add_butt.config(font=("arial", round(soft_title_f_size * 1.8)))
                soft_add_butt.pack(expand=True, fill=X)
                add_button_array.append(soft_add_butt)
                add_button_array[ch].bind("<Button-1>", lambda eff, soft_id_get=soft_list[ch]['id'], array_id_pass=ch:
                add_click(eff, soft_id=soft_id_get, array_id=array_id_pass))
                add_button_array[ch].bind("<Enter>", lambda eff, array_id_pass=ch:
                add_btn_on_hovering(eff, add_id=array_id_pass))
                add_button_array[ch].bind("<Leave>", lambda eff, array_id_pass=ch:
                add_but_return_to_normal_state(eff, add_id=array_id_pass))

                if str(select_box_array[ch]['state']) == 'disabled':
                    add_button_array[ch]['text'] = '-'

                ch += 1
        row_frame.pack(fill=X)


def select_box_change(event, array_id, soft_name):
    global select_box_array
    select_text_point = select_box_array[array_id].current()
    if select_text_point != -1:
        select_text = select_box_array[array_id].get()
        select_text_split = select_text.split('installed')
        if len(select_text_split) > 1:
            select_box_array[array_id].set('')
            showwarning("Warning", soft_name + " " + select_text_split[0] + "already installed")


def add_click(event, soft_id, array_id):
    global select_box_array, select_box_value_array, install_list, add_button_array
    select_text_point = select_box_array[array_id].current()
    if select_text_point != -1:
        add_log(log_types[2], "GuiCanvas.py",
                "add_click  soft_id : " + str(soft_id) + " event : " + str(event) + " array_id : " + str(array_id))
        ver_id_array = select_box_value_array[array_id]
        if len(ver_id_array) > 0:
            ver_id = ver_id_array[select_text_point]
            cr_array = {'soft_id': soft_id, 'ver_id': ver_id, 'select_text_point': select_text_point}
            if add_button_array[array_id]['text'] == '+':
                add_button_array[array_id]['text'] = '-'
                install_list.append(cr_array)
                select_box_array[array_id]['state'] = "disabled"
            else:
                add_button_array[array_id]['text'] = '+'
                install_list.remove(cr_array)
                select_box_array[array_id]['state'] = "readonly"
            # print(install_list)
        create_cart_labal()
    else:
        showinfo("Warning", "Select Software version")


def create_combobox(frame, soft, installed_list):
    global select_box_value_array
    ver_array = []
    ver_id_array = []
    for ver in Software().get_all_version(soft['id']):
        txt = "Ver : " + str(ver['v_no'])
        try:
            installed_list.index(ver['id'])
            txt += "  installed"
        except:
            txt += ""
        ver_array.append(txt)
        ver_id_array.append(ver['id'])

    select_box_value_array.append(ver_id_array)
    com_box = Combobox(frame, values=ver_array, font="bold", state="readonly")

    for add_soft in install_list:
        if add_soft['soft_id'] == soft['id']:
            com_box.current(add_soft['select_text_point'])
            com_box['state'] = 'disabled'
            break

    return com_box


def add_btn_on_hovering(event, add_id):
    global add_button_array
    add_log(log_types[2], "GuiMain.py", "add_btn_on_hovering : " + str(event))
    add_button_array[add_id]['bg'] = soft_add_butt_hover


def add_but_return_to_normal_state(event, add_id):
    global add_button_array
    add_log(log_types[2], "GuiMain.py", "add_but_return_to_normal_state : " + str(event))
    add_button_array[add_id]['bg'] = soft_add_butt_bg
