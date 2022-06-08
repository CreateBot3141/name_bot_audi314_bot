

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram
    label = 'send'

    message_out,menu = iz_telegram.get_message (user_id,'Найденный ответ:',namebot)
    #message_out = message_out.replace('%%Процент%%',str(minmin))   
    #message_out = message_out.replace('%%Заявка%%',str(command))

    name = 'не найдено'
    db,cursor = iz_func.connect ()
    sql = "select id,name from bot_product where namebot = '"+str(namebot)+"' and kod_1c = '"+str(message_in)+"' "
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data:
        id,name = rec.values()
        print ('[+] name:',name)
    markup = ''
    message_out = message_out.replace('%%name%%',str(name)) 
    answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
