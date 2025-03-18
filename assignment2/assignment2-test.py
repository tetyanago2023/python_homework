import assignment2 as a2
import os

def test_read_employees():
    employees = a2.read_employees()
    assert employees is not None
    assert a2.employees is not None
    assert len(a2.employees["fields"]) == 4
    assert a2.employees["fields"][1] == "first_name"
    assert len(a2.employees["rows"]) == 20

def test_column_name():
    assert a2.column_index("last_name") == 2
    assert a2.employee_id_column is not None

def test_first_name():
    assert a2.first_name(2) in ("David","Lauren") # values before and after sort

def test_employee_find():
    match = a2.employee_find(3)
    assert match[0][0] == "3"
    assert len(match[0]) == 4

def test_employee_find_2():
    match = a2.employee_find_2(4)
    assert match[0][0] == "4"
    assert len(match[0]) == 4

def test_sort_by_last_name():
    rows = a2.sort_by_last_name()
    assert len(rows) == 20
    assert rows[0][2]== "Bowman"

# def test_employee_dict():
#     dict_result = a2.employee_dict(a2.employees["rows"][0])
#     assert dict_result["last_name"] == "Bowman"
#     assert "employee_id" not in dict_result.keys()
#
# def test_all_employees_dict():
#     dict_result = a2.all_employees_dict()
#     assert len(dict_result.keys()) == 20
#     assert dict_result["9"]["first_name"] == "Phillip"
#
# def test_get_this_value():
#     assert a2.get_this_value() == "ABC"
#
# def test_set_that_secret():
#     import custom_module
#     a2.set_that_secret("swordfish")
#     assert custom_module.secret == "swordfish"
#
# def test_read_minutes():
#     d1, d2 = a2.read_minutes()
#     assert d1["rows"][1] == ("Tony Henderson","November 15, 1991")
#     assert d2["rows"][2] == ("Sarah Murray","November 19, 1988")
#     assert a2.minutes1 != None
#
# def test_create_minutes_set():
#     minutes_set = a2.create_minutes_set()
#     assert type(minutes_set).__name__ == "set"
#     assert len(minutes_set) == 46
#     assert a2.minutes_set != None
#
# def test_create_minutes_list():
#     minutes_list = a2.create_minutes_list()
#     assert type(minutes_list[0][1]).__name__ == "datetime"
#     assert type(minutes_list[0]).__name__ == "tuple"
#     assert a2.minutes_list != None
#
# def test_write_sorted_list():
#     sorted_list = a2.write_sorted_list()
#     assert sorted_list[0] == ("Jason Tucker","September 20, 1980")
#     assert os.access("./minutes.csv", os.F_OK) == True