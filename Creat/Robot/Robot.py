import Speak , tree
import Think , Listen
select = input("Lua chon cua ban la: ")
if select == "speak":
    tree.tree_speak()
elif select == "write":
    tree.tree_write()