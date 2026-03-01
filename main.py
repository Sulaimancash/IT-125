import flet
import functools

class EmployeesApp:
    def __init__(self, page: flet.Page):
        self.page = page
        self.page.title = "Каталог сотрудников"
        self.page.window_width = 600
        self.page.window_height = 700
        self.employees = []
        self.build_ui()

    def build_ui(self):
        self.page.add(flet.Text("Каталог сотрудников", size=22, weight="bold"))
        self.first_name = flet.TextField(label="Имя", width=400)
        self.last_name = flet.TextField(label="Фамилия", width=400)
        self.age = flet.TextField(label="Возраст", width=400, keyboard_type=flet.KeyboardType.NUMBER)
        self.salary = flet.TextField(label="Зарплата", width=400, keyboard_type=flet.KeyboardType.NUMBER)
        self.position = flet.Dropdown(
            label="Должность",
            width=400,
            options=[
                flet.dropdown.Option("Разработчик"),
                flet.dropdown.Option("Дизайнер"),
                flet.dropdown.Option("Менеджер"),
                flet.dropdown.Option("Ничего не делает но много зарабатывает"),
            ]
        )
        add_button = flet.ElevatedButton("Добавить сотрудника", on_click=self.add_employee)
        sort_button = flet.OutlinedButton("Сортировать по зарплате", on_click=self.sort_employees)
        self.result_text = flet.Text()
        self.list_column = flet.Column()
        self.page.add(
            self.first_name,
            self.last_name,
            self.age,
            self.salary,
            self.position,
            add_button,
            sort_button,
            self.result_text,
            flet.Divider(),
            self.list_column
        )

    def validate_data(self):
        if not all([self.first_name.value, self.last_name.value, self.age.value, self.salary.value, self.position.value]):
            return "Заполните все поля!"
        try:
            age = int(self.age.value)
            salary = int(self.salary.value)
        except ValueError:
            return "Возраст и зарплата должны быть числами!"
        if age < 18:
            return "Сотрудник должен быть старше 18 лет!"
        return None

    def add_employee(self, e):
        error = self.validate_data()
        if error:
            self.result_text.value = error
            self.result_text.color = "red"
        else:
            employee = {
                "first_name": self.first_name.value,
                "last_name": self.last_name.value,
                "age": int(self.age.value),
                "position": self.position.value,
                "salary": int(self.salary.value),
            }
            self.employees.append(employee)
            self.result_text.value = "Сотрудник добавлен!"
            self.result_text.color = "green"
            self.clear_form_fields()
            self.update_employee_list()
        self.page.update()

    def update_employee_list(self):
        self.list_column.controls.clear()
        for index, emp in enumerate(self.employees):
            salary_color = "green" if emp["salary"] > 100000 else "black"
            employee_row = flet.Row(
                controls=[
                    flet.Text(f'{emp["first_name"]} {emp["last_name"]} | {emp["position"]} | Возраст: {emp["age"]} | Зарплата: {emp["salary"]}', color=salary_color),
                    flet.IconButton(icon=flet.icons.DELETE, icon_color="red", on_click=functools.partial(self.delete_employee, index))
                ],
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN
            )
            self.list_column.controls.append(employee_row)

    def delete_employee(self, index, e=None):
        self.employees.pop(index)
        self.update_employee_list()
        self.page.update()

    def sort_employees(self, e):
        self.employees.sort(key=lambda x: x["salary"])
        self.update_employee_list()
        self.page.update()

    def clear_form_fields(self):
        self.first_name.value = ""
        self.last_name.value = ""
        self.age.value = ""
        self.salary.value = ""
        self.position.value = None

def main(page: flet.Page):
    EmployeesApp(page)

if __name__ == "__main__":
    flet.run(main)