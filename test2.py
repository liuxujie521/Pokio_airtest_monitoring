import requests

cookies = {
    'csrftoken': 'KQjMtz3qQKjVfeDTeDBAO6U9Ylszw43dyBNTJvNIic5GXKghfA0Bv5RVbGgHszMH',
    'sessionid': 'xv79w8klhx786l55ld6yrzpld51am387',
}

headers = {
    'Referer': 'http://192.168.101.176:8109/mg/mtt_official?tag1=mtt&tag2=match',
    'Proxy-Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQkvPO7NUiZVig4o7',
    'Origin': 'http://192.168.101.176:8109',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = '$------WebKitFormBoundaryQkvPO7NUiZVig4o7\\r\\nContent-Disposition: form-data; name="csrfmiddlewaretoken"\\r\\n\\r\\n3oUs7X393rCeM1t0dcGLU2X8rpvrigdDcJ9gpNTNcB2y3RIoL4FORRGJ51a4tEIX\\r\\n------WebKitFormBoundaryQkvPO7NUiZVig4o7\\r\\nContent-Disposition: form-data; name="image_logo"\\r\\n\\r\\nundefined\\r\\n------WebKitFormBoundaryQkvPO7NUiZVig4o7\\r\\nContent-Disposition: form-data; name="event_data"\\r\\n\\r\\n{"csrfmiddlewaretoken":"3oUs7X393rCeM1t0dcGLU2X8rpvrigdDcJ9gpNTNcB2y3RIoL4FORRGJ51a4tEIX","event_name":"","event_desc":"","game_type":"Holdem","binds_up":"7","start_stakes":"100","event_fee":"","service_fee":"","start_time":"","player_min":"","late_reg":"10","rebuy_times":"0","visibility":"4","alliance_id":"","club_id":"","event_gender":"2","blind_structure":"standard","table_size":"9","add_on":"0","is_halftime":"0","restrict_gps_ip":"0","hide_players_stats":"0","ticket_only":"0","break_time":"0","clone_switch":"0","is_mpc":"0","mtt_type":"3","series_day":"0","custom_payout_structure":"1","prize_guranteed":"","custom_payout_info":"[]","first_break_time_blind_level":0,"break_time_interval_level":0}\\r\\n------WebKitFormBoundaryQkvPO7NUiZVig4o7--\\r\\n'

response = requests.post('http://192.168.101.176:8109/static/bootstrap/fonts/glyphicons-halflings-regular.woff2', headers=headers, cookies=cookies, data=data, verify=False)
print(response.text)