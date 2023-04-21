{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red39\green129\blue201;\red0\green0\blue0;\red199\green203\blue211;
\red255\green255\blue255;\red235\green16\blue47;\red226\green131\blue14;\red20\green152\blue106;\red212\green20\blue102;
}
{\*\expandedcolortbl;;\cssrgb\c18039\c58431\c82745;\cssrgb\c0\c0\c0;\cssrgb\c81961\c83529\c85882;
\cssrgb\c100000\c100000\c100000;\cssrgb\c94902\c17255\c23922;\cssrgb\c91373\c58431\c4706;\cssrgb\c0\c65098\c49020;\cssrgb\c87451\c18824\c47451;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
def\cf4  \cf6 display\cf4 (contacts):\
    \cf2 for\cf4  i \cf2 in\cf4  \cf7 range\cf4 (\cf7 len\cf4 (contacts)):\
        \cf7 print\cf4 (\cf8 f"\{i+\cf9 1\cf8 \}. \{', '.join(contacts[i])\}"\cf4 )\
        \
\cf2 def\cf4  \cf6 add\cf4 (contacts):\
    name = \cf7 input\cf4 (\cf8 "Name: "\cf4 )\
    email = \cf7 input\cf4 (\cf8 "Email: "\cf4 )\
    phone = \cf7 input\cf4 (\cf8 "Phone: "\cf4 )\
    contact_id = \cf7 input\cf4 (\cf8 "ID: "\cf4 )\
    contact = [name, email, phone, contact_id]\
    contacts.append(contact)\
    \cf7 print\cf4 (\cf8 f"\{name\}, \{contact_id\} was added."\cf4 )\
\
\cf2 def\cf4  \cf6 view\cf4 (contacts):\
    contact_num = \cf7 int\cf4 (\cf7 input\cf4 (\cf8 f"Number (1 - \{\cf7 len\cf8 (contacts)\}): "\cf4 ))\
    \cf2 if\cf4  contact_num < \cf9 1\cf4  \cf2 or\cf4  contact_num > \cf7 len\cf4 (contacts):\
        \cf7 print\cf4 (\cf8 "Invalid number. Try again!"\cf4 )\
    \cf2 else\cf4 :\
        contact = contacts[contact_num-\cf9 1\cf4 ]\
        \cf7 print\cf4 (\cf8 f"\{', '.join(contact)\}"\cf4 )\
\
\cf2 def\cf4  \cf6 delete\cf4 (contacts):\
    contact_num = \cf7 int\cf4 (\cf7 input\cf4 (\cf8 f"Number (1 - \{\cf7 len\cf8 (contacts)\}): "\cf4 ))\
    \cf2 if\cf4  contact_num < \cf9 1\cf4  \cf2 or\cf4  contact_num > \cf7 len\cf4 (contacts):\
        \cf7 print\cf4 (\cf8 "Invalid number. Try again!"\cf4 )\
    \cf2 else\cf4 :\
        contact = contacts.pop(contact_num-\cf9 1\cf4 )\
        \cf7 print\cf4 (\cf8 f"\{', '.join(contact)\} was deleted."\cf4 )\
\
\cf2 def\cf4  \cf6 display_title\cf4 ():\
    \cf7 print\cf4 (\cf8 "Contact Management System"\cf4 )\
\
\cf2 def\cf4  \cf6 display_menu\cf4 ():\
    \cf7 print\cf4 (\cf8 "\\nCOMMAND MENU"\cf4 )\
    \cf7 print\cf4 (\cf8 "list - Display all contacts"\cf4 )\
    \cf7 print\cf4 (\cf8 "view - View a contact"\cf4 )\
    \cf7 print\cf4 (\cf8 "add - Add a contact"\cf4 )\
    \cf7 print\cf4 (\cf8 "del - Delete a contact"\cf4 )\
    \cf7 print\cf4 (\cf8 "exit - Exit program"\cf4 )\
\
\cf2 def\cf4  \cf6 main\cf4 ():\
    contacts = [\
        [\cf8 "Betty Johnson"\cf4 , \cf8 "betty.johnson@gmail.com"\cf4 , \cf8 "(408) 111-2222"\cf4 , \cf8 "3333"\cf4 ],\
        [\cf8 "Mark Arlington"\cf4 , \cf8 "mark.arlington@yahoo.com"\cf4 , \cf8 "(669) 123-4567"\cf4 , \cf8 "4444"\cf4 ]\
    ]\
    display_title()\
    display_menu()\
    \cf2 while\cf4  \cf2 True\cf4 :\
        command = \cf7 input\cf4 (\cf8 "\\nCommand: "\cf4 ).lower()\
        \cf2 if\cf4  command == \cf8 "list"\cf4 :\
            \cf7 print\cf4 ()\
            display(contacts)\
        \cf2 elif\cf4  command == \cf8 "view"\cf4 :\
            view(contacts)\
        \cf2 elif\cf4  command == \cf8 "add"\cf4 :\
            add(contacts)\
        \cf2 elif\cf4  command == \cf8 "del"\cf4 :\
            delete(contacts)\
        \cf2 elif\cf4  command == \cf8 "exit"\cf4 :\
            \cf7 print\cf4 (\cf8 "\\nThank you for using my app"\cf4 )\
            \cf2 break\cf4 \
        \cf2 else\cf4 :\
            \cf7 print\cf4 (\cf8 "Invalid command. Please try again."\cf4 )\
\
\cf2 if\cf4  __name__ == \cf8 "__main__"\cf4 :\
    main()}