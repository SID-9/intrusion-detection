import pickle
import streamlit as st

intrusion_model = pickle.load(open("D:\streamlit\intrusion_det\intrusion_detection_lor.sav","rb"))

# sidebar for navigation

nav = st.sidebar.radio("**NAVIGATION**",["welcome all !!","intrusion prediction system"])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

default_duration = 305.05410447761193
default_protocol_type = 0.5338599555414417
default_land = 7.939028262940616e-05
default_wrong_fragment = 0.023737694506192442
default_urgent = 3.969514131470308e-05
default_hot = 0.19803906001905366
default_num_failed_logins = 0.0011908542394410925
defalut_logged_in = 0.3947681803747221
default_num_compromised = 0.22785011114639567
default_root_shell = 0.0015481105112734202
default_su_attempted = 0.0013496348046999047
default_num_root = 0.2498412194347412
default_num_file_creations = 0.014726897427754843
default_num_shells = 0.0003572562718323277
default_num_access_files = 0.004326770403302636
default_num_outbound_cmds = 0.0
default_is_host_login = 0.0
default_is_guest_login = 0.009129882502381708
default_srv_count = 27.69875357256272
default_serror_rate = 0.28633772626230547
default_srv_serror_rate = 0.28376230549380754
default_rerror_rate = 0.11863012067322959
default_srv_rerror_rate = 0.12026040012702445
default_srv_diff_host_rate = 0.09593085106382979
default_dst_host_count = 182.53207367418227
default_dst_host_diff_srv_rate = 0.08253850428707526
default_dst_host_srv_diff_host_rate = 0.0318442362654811
default_dst_host_serror_rate = 0.28580025404890447
default_dst_host_srv_serror_rate = 0.27984637980311217
default_dst_host_rerror_rate = 0.11780009526833916
default_dst_host_srv_rerror_rate = 0.1187694506192442
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if nav=="intrusion prediction system":

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        duration = st.text_input("duration : ",value=default_duration)

    with col2:
        protocol_type = st.text_input("protocol_type : ",value=default_protocol_type)
    with col3:
        service = st.text_input("service : ")
    with col4:
        flag = st.text_input("flag:")

    
    with col1:
        src_bytes = st.text_input("src_bytes:")
    with col2:
        dst_bytes = st.text_input("dst_bytes:")
    with col3:
        land = st.text_input("land",value=default_land)
    with col4:
        wrong_fragment = st.text_input("wrong_fragment:",value=default_wrong_fragment)


    with col1:
        urgent = st.text_input("urgent:",value = default_urgent)
    with col2:
        hot  = st.text_input("hot:",value = default_hot)
    with col3:
        num_failed_logins = st.text_input("num_failed_logins:",value = default_num_failed_logins)
    with col4:
        logged_in = st.text_input("logged_in:",value = defalut_logged_in)
    

    with col1:
        num_compromised = st.text_input("num_compromised:",value = default_num_compromised )
    with col2:
        root_shell = st.text_input("root_shell : ",value = default_root_shell)
    with col3:
        su_attempted = st.text_input("su_attempted:",value = default_su_attempted )
    with col4:
        num_root = st.text_input("num_root:",value = default_num_root)


    with col1:
        num_file_creations = st.text_input("num_file_creations:",value = default_num_file_creations)
    with col2:
        num_shells = st.text_input("num_shells:",value = default_num_shells)
    with col3:
        num_access_files = st.text_input("num_access_files:",value = default_num_access_files)
    with col4:
        num_outbound_cmds = st.text_input("num_outbound_cmds:",value = default_num_outbound_cmds)


    with col1:
        is_host_login = st.text_input("is_host_login:",value = default_is_host_login)
    with col2:
        is_guest_login = st.text_input("is_guest_login:",value = default_is_guest_login)
    with col3:
        count= st.text_input("***count*** :")
    with col4:
        srv_count = st.text_input("srv_count : ",value = default_srv_count)
    

    with col1:
        serror_rate= st.text_input("serror_rate:",value=default_serror_rate)
    with col2:
        srv_serror_rate= st.text_input("srv_serror_rate :", value = default_srv_serror_rate)
    with col3:
        rerror_rate= st.text_input(" rerror_rate :",value = default_rerror_rate)
    with col4:
        srv_rerror_rate = st.text_input("srv_rerror_rate:",value=default_srv_rerror_rate)

    
    with col1:
        same_srv_rate= st.text_input("***same_srv_rate***:")
    with col2:
        diff_srv_rate= st.text_input("***diff_srv_rate*** :")
    with col3:
        srv_diff_host_rate = st.text_input("srv_diff_host_rate :",value = default_srv_diff_host_rate)
    with col4:
        dst_host_count = st.text_input("dst_host_count",value=default_dst_host_count)
    

    with col1:
        dst_host_srv_count= st.text_input("***dst_host_srv_count***:")
    with col2:
        dst_host_same_srv_rate= st.text_input("***dst_host_same_srv_rate*** :")
    with col3:
        dst_host_diff_srv_rate = st.text_input("dst_host_diff_srv_rate :",value = default_dst_host_diff_srv_rate)
    with col4:
        dst_host_same_src_port_rate = st.text_input("***dst_host_same_src_port_rate***:")


    with col1:
        dst_host_srv_diff_host_rate = st.text_input("dst_host_srv_diff_host_rate:",value=default_dst_host_srv_diff_host_rate)
    with col2:
        dst_host_serror_rate = st.text_input("dst_host_serror_rate :",value = default_dst_host_serror_rate)
    with col3:
        dst_host_srv_serror_rate = st.text_input("dst_host_srv_serror_rate :",value = default_dst_host_srv_serror_rate)
    with col4:
        dst_host_rerror_rate= st.text_input("dst_host_rerror_rat",value=default_dst_host_rerror_rate)

    with col1:
         dst_host_srv_rerror_rate = st.text_input("dst_host_srv_rerror_rat:",value=default_dst_host_srv_rerror_rate)


    rslt = ""
    if (st.button("detection test result")):
        id_predict = intrusion_model.predict([[duration,protocol_type,service,flag,src_bytes,
       dst_bytes, land, wrong_fragment,urgent,hot,
       num_failed_logins, logged_in, num_compromised, root_shell,
       su_attempted, num_root, num_file_creations, num_shells,
       num_access_files, num_outbound_cmds, is_host_login,
       is_guest_login, count, srv_count, serror_rate,
       srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate,
       diff_srv_rate, srv_diff_host_rate, dst_host_count,
       dst_host_srv_count, dst_host_same_srv_rate,
       dst_host_diff_srv_rate, dst_host_same_src_port_rate,
       dst_host_srv_diff_host_rate, dst_host_serror_rate,
       dst_host_srv_serror_rate, dst_host_rerror_rate,
       dst_host_srv_rerror_rate]])

        if(id_predict[0] == 1):
            rslt = "intrusion deteted"
        else:
            rslt = "no intrusion detected"
    st.success(rslt)
