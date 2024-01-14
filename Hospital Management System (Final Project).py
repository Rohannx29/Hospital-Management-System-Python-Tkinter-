from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class hospitalmanagementsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.patient_data = []

        self.NamePatient = StringVar()
        self.Age = StringVar()
        self.gender = StringVar()
        self.Disease = StringVar()
        self.BloodGroup = StringVar()
        self.NameDoctor = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red",
                         bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=510, y=130, width=520, height=280)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("times new roman", 12, "bold"),
                                   text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=480, height=240)

        # DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("times new roman", 12, "bold"),
        #                             text="Description")
        # DataframeRight.place(x=990, y=5, width=460, height=350)

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=415, width=1530, height=70)

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=490, width=1530, height=300)

        lblNamePatient = Label(DataframeLeft, text="Name Of Patient:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNamePatient.grid(row=0, column=0, sticky=W)
        txtNamePatient = Entry(DataframeLeft, textvariable=self.NamePatient, font=("arial", 13, "bold"), width=35)
        txtNamePatient.grid(row=0, column=1, sticky=W)

        lblAge = Label(DataframeLeft, text="Age:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAge.grid(row=1, column=0, sticky=W)
        txtAge = Entry(DataframeLeft, textvariable=self.Age, font=("arial", 13, "bold"), width=35)
        txtAge.grid(row=1, column=1, sticky=W)

        lblgender = Label(DataframeLeft, text="gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblgender.grid(row=2, column=0, sticky=W)
        comgender = ttk.Combobox(DataframeLeft, textvariable=self.gender, state="readonly",
                                 font=("arial", 12, "bold"), width=33)
        comgender['value'] = ("Male", "Female", "Others")
        comgender.current(0)
        comgender.grid(row=2, column=1, sticky=W)

        lblDisease = Label(DataframeLeft, text="Disease:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDisease.grid(row=3, column=0, sticky=W)
        txtDisease = Entry(DataframeLeft, textvariable=self.Disease, font=("arial", 13, "bold"), width=35)
        txtDisease.grid(row=3, column=1, sticky=W)

        lblBloodGrp = Label(DataframeLeft, text="Blood Group:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBloodGrp.grid(row=4, column=0, sticky=W)
        comBloodGrp = ttk.Combobox(DataframeLeft, textvariable=self.BloodGroup, state="readonly",
                                   font=("arial", 12, "bold"), width=33)
        comBloodGrp['value'] = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        comBloodGrp.current(0)
        comBloodGrp.grid(row=4, column=1, sticky=W)

        lblDrName = Label(DataframeLeft, text="Name Of Doctor:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDrName.grid(row=5, column=0, sticky=W)
        txtDrName = Entry(DataframeLeft, textvariable=self.NameDoctor, font=("arial", 13, "bold"), width=35)
        txtDrName.grid(row=5, column=1, sticky=W)

        # self.txtDescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        # self.txtDescription.grid(row=0, column=0)

        # btnDescription = Button(Buttonframe, text="Description", command=self.show_description, bg="green", fg="white",
        #                         font=("arial", 12, "bold"), width=28, height=16, padx=2, pady=6)
        # btnDescription.pack(side=LEFT)

        btnAddRec = Button(Buttonframe, text="Add Record", command=self.add_record, bg="green", fg="white",
                           font=("arial", 12, "bold"), width=48, height=16, padx=2, pady=6)
        btnAddRec.pack(side=LEFT)

        btnRemRec = Button(Buttonframe, text="Remove Record", command=self.remove_record, bg="green", fg="white",
                            font=("arial", 12, "bold"), width=50, height=16, padx=2, pady=6)
        btnRemRec.pack(side=LEFT)

        btnScrRec = Button(Buttonframe, text="Search Record", command=self.search_record, bg="green", fg="white",
                            font=("arial", 12, "bold"), width=48, height=16, padx=2, pady=6)
        btnScrRec.pack(side=RIGHT)

        # btnModRec = Button(Buttonframe, text="Modify Record", command=self.modify_record, bg="green", fg="white",
        #                     font=("arial", 12, "bold"), width=28, height=16, padx=2, pady=6)
        # btnModRec.pack(side=LEFT)

        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("Name Of Patient", "Age", "gender", "Disease",
                                                                  "Blood Group", "Name Of Doctor"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("Name Of Patient", text="Name Of Patient")
        self.hospital_table.heading("Age", text="Age")
        self.hospital_table.heading("gender", text="gender")
        self.hospital_table.heading("Disease", text="Disease")
        self.hospital_table.heading("Blood Group", text="Blood Group")
        self.hospital_table.heading("Name Of Doctor", text="Name Of Doctor")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        self.load_data()

    def load_data(self):
        # You can load data from a file or database here
        pass

    def show_entries(self):
        self.hospital_table.delete(*self.hospital_table.get_children())
        for entry in self.patient_data:
            self.hospital_table.insert("", "end", values=entry)

    # def show_description(self):
    #     self.txtDescription.delete(1.0, END)
    #     selected_item = self.hospital_table.selection()
    #     if selected_item:
    #         selected_index = int(selected_item[0])
    #         for field, value in zip(("Name Of Patient", "Age", "gender", "Disease", "Blood Group", "Name Of Doctor"),
    #                                 self.patient_data[selected_index]):
    #             self.txtDescription.insert(END, f"{field.ljust(20)}: {value}\n")

    def add_record(self):
        if self.validate_entries():
            record = [
                self.NamePatient.get(),
                self.Age.get(),
                self.gender.get(),
                self.Disease.get(),
                self.BloodGroup.get(),
                self.NameDoctor.get()
            ]
            self.patient_data.append(record)
            self.show_entries()

    def remove_record(self):
        if self.validate_entries():
            search_query = self.NamePatient.get().lower()
            found_records = [record for record in self.patient_data if search_query not in record[0].lower()]
            self.patient_data = found_records
            self.show_entries()

    def search_record(self):
        search_name = self.NamePatient.get().lower()
        search_age = self.Age.get().lower()
        search_gender = self.gender.get().lower()
        search_disease = self.Disease.get().lower()
        search_blood_group = self.BloodGroup.get().lower()
        search_doctor = self.NameDoctor.get().lower()

        filtered_records = [record for record in self.patient_data if
                            (search_name in record[0].lower()) and
                            (search_age in str(record[1]).lower()) and
                            (search_gender in record[2].lower()) and
                            (search_disease in record[3].lower()) and
                            (search_blood_group in record[4].lower()) and
                            (search_doctor in record[5].lower())]

        self.hospital_table.delete(*self.hospital_table.get_children())
        for entry in filtered_records:
            self.hospital_table.insert("", "end", values=entry)

    # def modify_record(self):
    #     selected_item = self.hospital_table.selection()
    #     if selected_item:
    #         selected_index = int(selected_item[0])

    #         # Modify the record in the existing window
    #         modify_window = Frame(self.root)
    #         modify_window.place(x=100, y=100, width=400, height=300)

    #         for i, (field, value) in enumerate(
    #                 zip(("Name Of Patient", "Age", "gender", "Disease", "Blood Group", "Name Of Doctor"),
    #                     self.patient_data[selected_index])):
    #             lbl = Label(modify_window, text=field, font=("arial", 12, "bold"))
    #             lbl.grid(row=i, column=0, sticky=W)
    #             entry = Entry(modify_window, font=("arial", 12))
    #             entry.insert(END, value)
    #             entry.grid(row=i, column=1, sticky=W)

    #         # Save changes button
    #         btn_save = Button(modify_window, text="Save Changes",
    #                           command=lambda: self.save_changes(modify_window, selected_index),
    #                           bg="green", fg="white", font=("arial", 12, "bold"))
    #         btn_save.grid(row=i + 1, columnspan=2, pady=10)

    # def save_changes(self, modify_window, selected_index):
    #     # Validate entries in the modification form
    #     new_record = []
    #     for entry_widget in modify_window.winfo_children():
    #         if isinstance(entry_widget, Entry):
    #             new_record.append(entry_widget.get())

    #     # Check if all fields are filled
    #     if all(new_record):
    #         # Update the table and patient_data
    #         self.hospital_table.item(selected_index, values=new_record)
    #         self.patient_data[selected_index] = new_record
    #         modify_window.destroy()
    #     else:
    #         messagebox.showerror("Error", "All fields must be filled.")

    def validate_entries(self):
        if not all((self.NamePatient.get(), self.Age.get(), self.gender.get(), self.Disease.get(),
                    self.BloodGroup.get(), self.NameDoctor.get())):
            messagebox.showerror("Error", "All entries are mandatory.")
            return False
        return True

root = Tk()
ob = hospitalmanagementsystem(root)
root.mainloop()
