import gui
import db
import check


def start():
    db.save_info(gui.get_input())
    data = db.get_info()
    result = check.check(data)
    db.save_result(result)
    gui.send_info(result)
    db.log(data, result)