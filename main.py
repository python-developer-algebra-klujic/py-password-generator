import random as rd
import tkinter as tk


#region Funkcije
def generate_password():
    # posebni znakovi   33-47 | 58-64 | 91-96 | 123 - 126
    # brojevi           48-57
    # slova             65-90 | 97-122
    # sve               33-126
    password = ''
    password_length = scl_password_length_var.get()

    for _ in range(password_length):
        if cb_letters_only_var.get() and cb_sp_characters_only_var.get():
            rnd_char_number_range = rd.choice([(65, 90), (97, 122), (33,47), (58, 64), (91, 96), (123, 126)])
        elif cb_letters_only_var.get() and cb_numbers_only_var.get():
            rnd_char_number_range = rd.choice([(48, 57), (65, 90), (97, 122)])
        elif cb_numbers_only_var.get():
            rnd_char_number_range = rd.choice([(48, 57)])
        elif cb_sp_characters_only_var.get():
            rnd_char_number_range = rd.choice([(33,47), (58, 64), (91, 96), (123, 126)])
        else:
            rnd_char_number_range = rd.choice([(33, 126)])

        rnd_char_number = rd.randint(*rnd_char_number_range)
        rnd_char = chr(rnd_char_number)
        password += rnd_char


    ent_display_password_var.set(password)


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(ent_display_password_var.get())


def reset():
    ent_display_password_var.set('')


def toggle_display_password():
    if rb_password_var.get() == 'display':
        ent_display_password.config(show="")
    else:
        ent_display_password.config(show="*")

#endregion




root = tk.Tk()
root.title('Algebra - Python Password Generator')
# root.geometry('600x400')

#region Naslovna labela
lbl_title = tk.Label(root,
                     text='Password Generator',
                     font=('Verdana', 20))
lbl_title.grid(column=0, columnspan=3, row=0,
               padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Postavke frame
lbl_frm_settings = tk.LabelFrame(root, text='Settings')
lbl_frm_settings.grid(column=0, columnspan=3, row=1,
                  padx=10, pady=10, ipadx=5, ipady=5)


cb_letters_only_var = tk.BooleanVar()
cb_letters_only = tk.Checkbutton(lbl_frm_settings,
                                 text='Samo slova',
                                 variable=cb_letters_only_var)
cb_letters_only.grid(column=0, row=0,
                     padx=10, pady=10, ipadx=5, ipady=5)

cb_numbers_only_var = tk.BooleanVar()
cb_numbers_only = tk.Checkbutton(lbl_frm_settings,
                                 text='Samo brojevi',
                                 variable=cb_numbers_only_var)
cb_numbers_only.grid(column=1, row=0,
                     padx=10, pady=10, ipadx=5, ipady=5)

cb_sp_characters_only_var = tk.BooleanVar()
cb_sp_characters_only = tk.Checkbutton(lbl_frm_settings,
                                       text='Samo posebni znakovi',
                                       variable=cb_sp_characters_only_var)
cb_sp_characters_only.grid(column=2, row=0,
                           padx=10, pady=10, ipadx=5, ipady=5)



rb_password_var = tk.StringVar(value='display')
rb_display_password = tk.Radiobutton(lbl_frm_settings,
                                     text='Prikazi lozinku',
                                     variable=rb_password_var,
                                     value='display',
                                     command=toggle_display_password)
rb_display_password.grid(column=0, columnspan=2, row=1,
                         padx=10, pady=10, ipadx=5, ipady=5)


rb_hide_password = tk.Radiobutton(lbl_frm_settings,
                                  text='Sakrij lozinku',
                                  variable=rb_password_var,
                                  value='hide',
                                  command=toggle_display_password)
rb_hide_password.grid(column=2, row=1,
                      padx=10, pady=10, ipadx=5, ipady=5)



scl_password_length_var = tk.IntVar(value=10)
scl_password_length = tk.Scale(lbl_frm_settings,
                               orient='horizontal',
                               length=300,
                               variable=scl_password_length_var,
                               from_=8,
                               to=40)
scl_password_length.grid(column=0, columnspan=3, row=2,
                         padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Gumbi
btn_generate_password = tk.Button(root,
                                  text='Generiraj lozinku',
                                  command=generate_password)
btn_generate_password.grid(column=0, row=2,
                           padx=10, pady=10, ipadx=5, ipady=5)

btn_copy_password = tk.Button(root,
                              text='Kopiraj lozinku',
                              command=copy_password)
btn_copy_password.grid(column=1, row=2,
                       padx=10, pady=10, ipadx=5, ipady=5)

btn_reset = tk.Button(root,
                      text='Resetiraj',
                      command=reset)
btn_reset.grid(column=2, row=2,
               padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Generirana lozinka
ent_display_password_var = tk.StringVar(value='')
ent_display_password = tk.Entry(root,
                                bd=0,
                                textvariable=ent_display_password_var,
                                width=45,
                                justify='center',
                                background='systembuttonface',
                                font=('Verdana', 25))
ent_display_password.grid(column=0, columnspan=3, row=3,
                          padx=10, pady=30, ipadx=5, ipady=5)
#endregion


root.mainloop()
