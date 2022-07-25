import csv
import string
import random
import json
from faker import Faker

airtel_data='''{
   "butterfly": {
      "requestid": "3",
      "operation": "AccountCreate",
      "cust_ac_no": "ATOPJ6450C12",
      "customer": {
         "parent_ac_no": "par992",
         "root_ac_no": "rot66dse",
         "income_lvl": "",
         "pymnt_mthd": "check",
         "source_systm": "",
         "bill_prd": "15KK-Delhi Monthly 13th",
         "cust_create_dt": "20191007000000",
         "cust_act_dt": "20180922080932",
         "cust_stts": "sts2",
         "fname": "Saurabh",
         "mname": "Patel",
         "cust_seg": "11",
         "cust_cat": "",
         "crdt_rtng": "0",
         "cors_addrss": {
            "address1": "",
            "address2": "",
            "address3": "",
            "address4": "",
            "landmark": "P",
            "district": "",
            "city": "",
            "country": "",
            "state": "",
            "pincode": "560025"
         },
         "org_name": "",
         "res_addrss": {
            "address1": "102",
            "address2": "Sobha pearl",
            "address3": "",
            "address4": "",
            "landmark": "",
            "district": "",
            "city": "",
            "country": "india",
            "state": "",
            "pincode": "560025"
         },
         "nationality": "indian",
         "lname": "k",
         "prename": "miss",
         "email": "ATOPJ6450D12@airtel.com",
         "gender": "F",
         "value_type": "GoldNew",
         "vipflag": "",
         "pref_comm_ch": "",
         "org_type": "",
         "cust_qual": "",
         "occupation": "",
         "pan": "ATOPJ6450C12",
         "marital_stts": "",
         "self_pay_mode": "",
         "risk_profile": "",
         "dob": "",
         "biz_unit": "",
         "cust_type": "b2b",
         "van": "van53",
         "cust_class": "",
         "market_seg": "Default",
         "prod_type": "",
         "pref_comm_lang": "",
         "pref_med_type": "",
         "rtn": "",
         "crdt_limit": "123",
         "date_mar": "",
         "is_billable": "bil12",
         "ba_gst": "GST091",
         "tan": "TAN001",
         "cin": "CIN001",
         "cntct_info": [
            {
               "cntct_id": "12345",
               "cntct_typ": "Autho",
               "prmry_flg": "01",
               "frst_nm": "First name",
               "mddl_nm": "fmname",
               "lst_nm": "lstname",
               "cnt": "47987987798",
               "eml_addr": "ATOPJ6450d12@airtel.com",
               "ebll_flg": "0/1",
               "dsgntn": "Designation"
            }
         ],
         "is_si_acc": "0",
         "prmry_van": "1"
      },
      "service": {
         "circle": "DELHI",
         "circle_id": "Delhi",
         "is_tata": "",
         "si_sts": "NEW",
         "act_date": "",
         "msisdn": "9931459800",
         "imsi": "9769752497697",
         "srvc_ins_type": "",
         "inst_addrss": {
            "address1": "",
            "address2": "",
            "address3": "",
            "address4": "",
            "landmark": "",
            "district": "",
            "city": "",
            "country": "",
            "state": "KAR",
            "pincode": "560025"
         },
         "type_lte": "Y",
         "sim_no": "",
         "sim_type": "ESIM",
         "pckg": {
            "id": "",
            "dbr_mode": "",
            "act_ts": "",
            "org_deact_ts": "",
            "eff_deact_ts": "20190927000000",
            "name": "",
            "price": ""
         },
         "fnft": "Outstation",
         "adh_rever_date": "20180922080932",
         "ekycready": "YES",
         "ref_aadhaar": "",
         "adh_acquired": "YES",
         "volteflag": "Y",
         "ivr_lang": "Hin",
         "bill_pn_name": "",
         "bill_pn_rent": "GSM Mobile Delhi",
         "bill_plan_typ": "",
         "bill_acc_id": "12345",
         "is_parent": "Y",
         "parent_msisdn": "23456781",
         "isd": "91",
         "oadate": "",
         "s_si": "",
         "s_imei": "",
         "s_imsi": "404497770061946",
         "s_iccid": "8991401877700109083F",
         "hasiwatch": "1"
      }
   }
}'''
def return_argumentlist():
    with open("robofiles/header.csv",'r') as csv_file:
        csv_reader=csv.reader(csv_file)

        for line in csv_reader:
            last=line
        return last

# for each line

def return_json(given,given_length, given_type, pre="", post=""):
    data = json.loads(airtel_data)

    n = len(pre)
    given_length=int(given_length)
    if n == 0:
        n = len(post)
    z = given_length - n




    if given_type == "numeric":

        res = ''.join(random.choices(string.digits, k=z))

    elif given_type == "alphanumeric":
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=z))

    else:
        res = ''.join(random.choices(string.ascii_letters, k=z))

    change_to = pre + res + post
    lst = given.split(".")
    new_lst = ["butterfly"]
    for elt in lst:
        new_lst.append(elt)

    last = new_lst.pop()
    final = data
    for elt in new_lst:
        final = final[elt]
    final[last] = change_to
    z = json.dumps(data)
    return z


z=return_json(*return_argumentlist())
print(z)


















