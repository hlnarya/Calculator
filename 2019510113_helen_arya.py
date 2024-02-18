try :
    fin= open("input.txt","r" ,encoding ="utf8") 
    
except FileNotFoundError:
    print('Can\'t find file or read data')   
    
except IOError:
    print('An error happened, please try again') 
    
else:
    
    try:
        file_name = "2019510113_helen_arya_output.txt"
        fw = open(file_name, "w+")  
        
    except FileExistsError:
        print('An error happened, please try again')   
        
    except IOError:
        print('An error happened, please try again') 
        
    except ValueError:
        print('An error happened, please try again')   
        
    else:
      
        list_numbers=['0','1','2','3','4','5','6','7','8','9']
        list_real_op=['*','**','/','//','%','-','+','>','<','==','!=','>=','<=']
        list_operator=['=','!','>','<','*','/','%','+','-']
        list_logical=['>','<','==','!=','>=','<=']
        l_second =[] # ijad yek list khali 
        L=[] #oon aslie hast 

        fin= open("input.txt","r")
        file_name2 = "2019510113_helen_arya_output.txt"    
        fw = open(file_name2, "w")  
        for line in fin:
            L.clear()
            string = line.strip() 
            l_first=list(string) 
           


            flag_error=False
            flag_power=False
            flag_division=False 
            flag_kb=False
            flag_bk=False
            flag_empty=False
            if len(l_first)==0:
                flag_empty=True
                fw.write("\n")
           
            if len(l_first) !=0:
                if list_numbers.count(l_first[0]) == 0 and list_numbers.count(l_first[-1]) != 0  :
                    flag_error=True
                    fw.write("ERROR\n")
                if list_numbers.count(l_first[0]) != 0  and list_numbers.count(l_first[-1]) == 0 :
                    flag_error=True
                    fw.write("ERROR\n")
                if list_numbers.count(l_first[0]) == 0  and list_numbers.count(l_first[-1]) == 0 :
                    flag_error=True
                    fw.write("ERROR\n")
           
           
            if flag_error == False:
                for i in range(0,len(l_first)): 
                    
                    if  l_first[i] != ' ' and  list_numbers.count(l_first[i]) == 0 and list_operator.count(l_first[i])==0:
                        flag_error=True
                    
                   
                    if i==0 and list_numbers.count(l_first[i]) !=0  :            
                        nums=l_first[0]    
                      
                    if i>=1:
                        #print(i)
                        
                        if list_numbers.count(l_first[i]) !=0  :
                            
                            if list_numbers.count(l_first[i-1])!=0:
                                
                                nums=nums+l_first[i]
                            else:
                                nums=l_first[i]
                        else:
                            if list_numbers.count(l_first[i-1])!=0:
                                l_second.append(nums)
                                
                                nums=''
                   
                                   
                        if flag_kb == False:
                           if list_operator.count(l_first[i])!= 0 :
                            if l_first[i]== '<':
                             if (l_first[i+1]==' '  or list_numbers.count(l_first[i+1])!=0) and (l_first[i-1]!='=' ) :            
                                l_second.append('<')            
                                 
                        if list_operator.count(l_first[i])!= 0 :
                          if l_first[i]== '<':
                            if l_first[i+1]=='=' :
                               flag_kb==True
                               l_second.append(l_first[i]+l_first[i+1]) 
                               
                                    
                        if flag_bk == False:
                            if list_operator.count(l_first[i])!= 0 :
                             if l_first[i]== '>':
                                if (l_first[i+1]==' '  or list_numbers.count(l_first[i+1])!=0) and (l_first[i-1]!='=' ) :            
                                   l_second.append('>')            
                                     
                        if list_operator.count(l_first[i])!= 0 :
                             if l_first[i]== '>':
                               if l_first[i+1]=='=' :
                                  flag_bk==True
                                  l_second.append(l_first[i]+l_first[i+1]) 
                                  
                                  
                        if list_operator.count(l_first[i])!= 0 :
                            if l_first[i]== '=':
                                if l_first[i-1]=='!' or l_first[i-1]=='=' :
                                    l_second.append(l_first[i-1]+l_first[i])          
                                  
                        if list_operator.count(l_first[i])!= 0 :
                              if ((l_first[i]== '=')  and (list_numbers.count(l_first[i-1])!=0 or  list_operator.count(l_first[i-1])!= 0 or l_first[i-1]==' ') and (l_first[i-1]!='>' and l_first[i-1]!='<' and l_first[i-1]!='!'  and l_first[i-1]!='=' and l_first[i+1]!='='))   :
                                  l_second.append('=')
                         
                        if list_operator.count(l_first[i])!= 0 :
                               if l_first[i]== '!' and l_first[i+1]!='=':
                                   l_second.append('!')            
                                   
                                   
                        if flag_power==False :
                              if list_operator.count(l_first[i])!= 0 :
                                  if l_first[i]== '*':
                                      if (l_first[i-1]==' '  or list_numbers.count(l_first[i-1])!=0 or  list_operator.count(l_first[i-1])!= 0) and ((l_first[i+1]!='*' ) and (l_first[i-1]!='*')  )  : 
                                          if l_first[i+1]!='*' :
                                           l_second.append('*')            
                                     
                        if list_operator.count(l_first[i])!= 0 :
                           if l_first[i]== '*':
                               if l_first[i-1]=='*' :
                                   flag_power==True
                                   l_second.append(l_first[i-1]+l_first[i])    
                               
                        if flag_division==False :
                              if list_operator.count(l_first[i])!= 0 :
                                  if l_first[i]== '/':
                                      if (l_first[i-1]==' '  or list_numbers.count(l_first[i-1])!=0 or  list_operator.count(l_first[i-1])!= 0) and ((l_first[i+1]!='/' ) and (l_first[i-1]!='/') ) :            
                                          l_second.append('/')           
                   
                        if list_operator.count(l_first[i])!= 0 :
                           if l_first[i]== '/':
                               if l_first[i-1]=='/' :
                                  flag_division==True
                                  l_second.append(l_first[i-1]+l_first[i])
                               
                                                        
                        if list_operator.count(l_first[i])!= 0 :
                            if l_first[i]== '%':
                                l_second.append('%') 
                              
                        if list_operator.count(l_first[i])!= 0 :
                             if l_first[i]== '+':
                                 l_second.append('+')                
                                 
                        if list_operator.count(l_first[i])!= 0 :
                              if l_first[i]== '-':
                                  l_second.append('-') 
                       
                            
                     
                    if i==len(l_first)-1 and nums!='':
                        l_second.append(nums) 
                        
                        
                for i in range(0,len(l_second)-1): #baraye taghsim 
                    if(l_second[i]=='/' and l_second[i+1]=='0'):
                        flag_error=True  
                    if(l_second[i]=='//' and l_second[i+1]=='0'):
                        flag_error=True 
                    if(l_second[i]=='%' and l_second[i+1]=='0'):
                        flag_error=True 
                    if list_numbers.count(l_second[i])!=0 and list_numbers.count(l_second[i+1])!=0 : #baraye 2 ta adad posht sare ham
                        flag_error=True 
                    if( list_real_op.count(l_second[i])!=0 and  list_real_op.count(l_second[i+1])!=0): #vase kenare ham boodane har do operatori
                        flag_error=True
                    if( list_operator.count(l_second[i])!=0 and  list_operator.count(l_second[i+1])!=0): #vase kenare ham boodane har do operatori
                         flag_error=True  

                for j in range(0,len(list_logical)): #vase shemordane tedade logicalha
                    if l_second.count(list_logical[j])>1:
                        flag_error=True
                        L.clear()  
                    if l_second.count('>')!=0 and (l_second.count('<')!=0 or l_second.count('==')!=0 or l_second.count('!=')!=0 or l_second.count('>=')!=0 or l_second.count('<=')!=0):
                        flag_error=True
                        L.clear() 
                    if l_second.count('<')!=0 and (l_second.count('>')!=0 or l_second.count('==')!=0 or l_second.count('!=')!=0 or l_second.count('>=')!=0 or l_second.count('<=')!=0):
                        flag_error=True
                        L.clear()
                    if l_second.count('==')!=0 and (l_second.count('<')!=0 or l_second.count('>')!=0 or l_second.count('!=')!=0 or l_second.count('>=')!=0 or l_second.count('<=')!=0):
                        flag_error=True
                        L.clear()
                    if l_second.count('!=')!=0 and (l_second.count('<')!=0 or l_second.count('==')!=0 or l_second.count('>')!=0 or l_second.count('>=')!=0 or l_second.count('<=')!=0):
                        flag_error=True
                        L.clear()
                    if l_second.count('>=')!=0 and (l_second.count('<')!=0 or l_second.count('==')!=0 or l_second.count('!=')!=0 or l_second.count('>')!=0 or l_second.count('<=')!=0):
                        flag_error=True
                        L.clear()
                    if l_second.count('<=')!=0 and (l_second.count('<')!=0 or l_second.count('==')!=0 or l_second.count('!=')!=0 or l_second.count('>=')!=0 or l_second.count('>')!=0):
                        flag_error=True
                        L.clear()
                    else:
                        L=l_second
                        
                for j in range(0,len(l_second)-1): 
                    if str(l_second[j]).isdigit() and str(l_second[j+1]).isdigit():
                          flag_error=True
                
               # print(l_second)
               # print("inja error" ,flag_error)
                
                
                if  flag_error==False:
                    count=0
                    for i in range(0,len(L)-2):
                       
                        if L[i+1] =='**':
                            
                            result=float(L[i]) ** float(L[i+2])
                           # print(result)
                            
                            del L[i:i+3]
                            
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                            L.insert(i+2,str(result))
                           
                            
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                         
                      

                          
                    count=0
                    for i in range(0,len(L)-2):       
                            
                        if L[i+1] =='*':
                                  
                            result=float(L[i]) * float( L[i+2])
                           # print(result)
                            
                            del L[i:i+3]
                            
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                            L.insert(i+2,str(result))
                                       
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                               
                       
                        

                    count=0     
                    for i in range(0,len(L)-2):       
                            
                        if L[i+1] =='/':
                            
                            result=float(L[i]) / float(L[i+2])
                          #  print(result)
                            
                            del L[i:i+3]
                            
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                          
                            L.insert(i+2,str(result))
                                 
                           
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                                 
                     
                               
                    count=0 
                    for i in range(0,len(L)-2):       
                            
                        if L[i+1] =='//':
                           
                            result=float(L[i]) // float( L[i+2])
                           # print(result)
                            
                            del L[i:i+3]
                            
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                            L.insert(i+2,str(result))
                                 
                          
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                      

                           
                    count=0
                    for i in range(0,len(L)-2):       
                            
                        if L[i+1] =='%':
                            
                            
                            result=float(L[i]) % float( L[i+2])
                           # print(result)
                            
                            del L[i:i+3]
                            
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                            L.insert(i+2,str(result))
                                 
                           
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                        

                              
                    count=0         
                    for i in range(0,len(L)-2):       
                             
                         if L[i+1] =='+':      
                             
                             result=float(L[i]) + float( L[i+2])
                           #  print(result)
                             
                             del L[i:i+3]
                             
                             L.insert(i,str(' @ '))
                             count=count+1
                             L.insert(i+1,str(' @ '))
                             count=count+1
                             L.insert(i+2,str(result))
                                   
                           
                    for j in range(1,count+1):    
                        L.remove(' @ ')
                                   
                       
                                      
                    count=0    
                    for i in range(0,len(L)-2):       
                               
                         if L[i+1] =='-':
                           
                            result=float(L[i]) - float( L[i+2])
                          #  print(result)
                               
                            del L[i:i+3]
                               
                            L.insert(i,str(' @ '))
                            count=count+1
                            L.insert(i+1,str(' @ '))
                            count=count+1
                            L.insert(i+2,str(result))
                                       
                           
                    for j in range(1,count+1):    
                        L.remove(' @ ')


                   
                    if flag_error==False and flag_empty==False:
                        if (L[len(L)-1] == '==') and (float(L[len(L)-2]) == float(L[len(L)])) :
                            flage_logic=True
                            fw.write("True\n") 
                            L.clear()                   
                        elif (L[len(L)-1] == '>=') and (float(L[len(L)-2]) >= float(L[len(L)])) :
                            flage_logic=True
                            fw.write("True\n")
                            L.clear() 
                        elif (L[len(L)-1] == '<=') and (float(L[len(L)-2]) <= float(L[len(L)])) :
                            flage_logic=True
                            fw.write("True\n")
                            L.clear() 
                        elif (L[len(L)-1]== '>') and (float(L[len(L)-2]) > float(L[len(L)])) :
                             flage_logic=True
                             fw.write("True\n")
                             L.clear() 
                        elif (L[len(L)-1] == '<') and (float(L[len(L)-2]) < float(L[len(L)])) :
                             flage_logic=True
                             fw.write("True\n") 
                             L.clear() 
                        elif (L[len(L)-1] == '!=') and (float(L[len(L)-2]) != float(L[len(L)])) :
                             flage_logic=True
                             fw.write("True\n") 
                             L.clear()                     
                        elif (L[len(L)-1] == '==') and (float(L[len(L)-2]) != float(L[len(L)])) :
                             flage_logic=False
                             fw.write("False\n")
                             L.clear()                     
                        elif (L[len(L)-1] == '>=') and (float(L[len(L)-2]) < float(L[len(L)])) :
                             flage_logic=False
                             fw.write("False\n")
                             L.clear() 
                        elif (L[len(L)-1] == '<=') and (float(L[len(L)-2]) > float(L[len(L)])) :
                             flage_logic=False
                             fw.write("False\n")
                             L.clear() 
                        elif (L[len(L)-1] == '>') and (float(L[len(L)-2]) <= float(L[len(L)])) :
                             flage_logic=False
                             fw.write("False\n")
                             L.clear() 
                        elif (L[len(L)-1] == '<') and (float(L[len(L)-2]) >= float(L[len(L)])) :
                             flage_logic=False
                             fw.write("False\n") 
                             L.clear() 
                        elif (L[len(L)-1] == '!=') and (float(L[len(L)-2]) == float(L[len(L)])) :
                             flage_logic=False 
                             fw.write("False\n")
                             L.clear()
                        for k in range(0,len(L)-2):
                            if (L[k+1] == '==') and (float(L[k]) == float(L[k+2])) :
                                flage_logic=True
                                fw.write("True\n") 
                                L.clear()                   
                            elif (L[k+1] == '>=') and (float(L[k]) >= float(L[k+2])) :
                                flage_logic=True
                                fw.write("True\n")
                                L.clear() 
                            elif (L[k+1] == '<=') and (float(L[k]) <= float(L[k+2])) :
                                flage_logic=True
                                fw.write("True\n")
                                L.clear() 
                            elif (L[k+1] == '>') and (float(L[k]) > float(L[k+2])) :
                                 flage_logic=True
                                 fw.write("True\n")
                                 L.clear() 
                            elif (L[k+1] == '<') and (float(L[k]) < float(L[k+2])) :
                                 flage_logic=True
                                 fw.write("True\n") 
                                 L.clear() 
                            elif (L[k+1] == '!=') and (float(L[k]) != float(L[k+2])) :
                                 flage_logic=True
                                 fw.write("True\n") 
                                 L.clear()                     
                            elif (L[k+1] == '==') and (float(L[k]) != float(L[k+2])) :
                                 flage_logic=False
                                 fw.write("False\n")
                                 L.clear()                     
                            elif (L[k+1] == '>=') and (float(L[k]) < float(L[k+2])) :
                                 flage_logic=False
                                 fw.write("False\n")
                                 L.clear() 
                            elif (L[k+1] == '<=') and (float(L[k]) > float(L[k+2])) :
                                 flage_logic=False
                                 fw.write("False\n")
                                 L.clear() 
                            elif (L[k+1] == '>') and (float(L[k]) <= float(L[k+2])) :
                                 flage_logic=False
                                 fw.write("False\n")
                                 L.clear() 
                            elif (L[k+1] == '<') and (float(L[k]) >= float(L[k+2])) :
                                 flage_logic=False
                                 fw.write("False\n") 
                                 L.clear() 
                            elif (L[k+1] == '!=') and (float(L[k]) == float(L[k+2])) :
                                 flage_logic=False 
                                 fw.write("False\n")
                                 L.clear()
                    if flag_error==True:
                        L.clear()
                    for i in range(0,len(L)):
                        fw.write(str(L[i])+"\n")
                                    
                else:
                    if flag_empty==False:
                        fw.write("ERROR\n")
                    
                           
        fin.close()
        fw.close()         
         
    finally:          
        print(" ")        


finally:          
       print("Thank you for using my application!!")     





















