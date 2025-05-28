import random as rd
import customtkinter as ctk
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
        elif cb_letters_only_var.get():
            rnd_char_number_range = rd.choice([(65, 90), (97, 122),])
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
        ent_display_password.configure(show="")
    else:
        ent_display_password.configure(show="*")

#endregion


root = ctk.CTk()
root.title('Algebra - Python Password Generator')
root.geometry('600x400')
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")
# ctk.set_appearance_mode("system")  # default
# ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("light")


#region Naslovna labela
lbl_title = ctk.CTkLabel(root,
                     text='Password Generator',
                     font=('Verdana', 20))
lbl_title.grid(column=0, columnspan=3, row=0,
               padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Postavke frame
lbl_frm_settings = ctk.CTkFrame(root)
lbl_frm_settings.grid(column=0, columnspan=3, row=1,
                  padx=10, pady=10, ipadx=5, ipady=5)


cb_letters_only_var = ctk.BooleanVar()
cb_letters_only = ctk.CTkCheckBox(lbl_frm_settings,
                                 text='Samo slova',
                                 variable=cb_letters_only_var)
cb_letters_only.grid(column=0, row=0,
                     padx=10, pady=10, ipadx=5, ipady=5)

cb_numbers_only_var = ctk.BooleanVar()
cb_numbers_only = ctk.CTkCheckBox(lbl_frm_settings,
                                 text='Samo brojevi',
                                 variable=cb_numbers_only_var)
cb_numbers_only.grid(column=1, row=0,
                     padx=10, pady=10, ipadx=5, ipady=5)

cb_sp_characters_only_var = ctk.BooleanVar()
cb_sp_characters_only = ctk.CTkCheckBox(lbl_frm_settings,
                                       text='Samo posebni znakovi',
                                       variable=cb_sp_characters_only_var)
cb_sp_characters_only.grid(column=2, row=0,
                           padx=10, pady=10, ipadx=5, ipady=5)



rb_password_var = ctk.StringVar(value='display')
rb_display_password = ctk.CTkRadioButton(lbl_frm_settings,
                                     text='Prikazi lozinku',
                                     variable=rb_password_var,
                                     value='display',
                                     command=toggle_display_password)
rb_display_password.grid(column=0, columnspan=2, row=1,
                         padx=10, pady=10, ipadx=5, ipady=5)


rb_hide_password = ctk.CTkRadioButton(lbl_frm_settings,
                                  text='Sakrij lozinku',
                                  variable=rb_password_var,
                                  value='hide',
                                  command=toggle_display_password)
rb_hide_password.grid(column=2, row=1,
                      padx=10, pady=10, ipadx=5, ipady=5)



scl_password_length_var = ctk.IntVar(value=10)
scl_password_length = ctk.CTkSlider(lbl_frm_settings,
                               orientation='horizontal',
                               width=300,
                               variable=scl_password_length_var,
                               from_=8,
                               to=40)
scl_password_length.grid(column=0, columnspan=3, row=2,
                         padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Gumbi
btn_generate_password = ctk.CTkButton(root,
                                  text='Generiraj lozinku',
                                  command=generate_password)
btn_generate_password.grid(column=0, row=2,
                           padx=10, pady=10, ipadx=5, ipady=5)

btn_copy_password = ctk.CTkButton(root,
                              text='Kopiraj lozinku',
                              command=copy_password)
btn_copy_password.grid(column=1, row=2,
                       padx=10, pady=10, ipadx=5, ipady=5)

btn_reset = ctk.CTkButton(root,
                      text='Resetiraj',
                      command=reset)
btn_reset.grid(column=2, row=2,
               padx=10, pady=10, ipadx=5, ipady=5)
#endregion


#region Generirana lozinka
ent_display_password_var = ctk.StringVar(value='')
ent_display_password = ctk.CTkEntry(root,
                                textvariable=ent_display_password_var,
                                width=450,
                                justify='center',
                                font=('Verdana', 25))
ent_display_password.grid(column=0, columnspan=3, row=3,
                          padx=10, pady=30, ipadx=5, ipady=5)
#endregion


root.mainloop()
