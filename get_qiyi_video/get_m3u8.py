import requests
import re
import json

url = "https://cache.video.iqiyi.com/jp/dash?tvid=14272431000&bid=200&vid=ab70b61f9fbd919274274ee89e246f8c&src=01010031010000000000&vt=0&rs=1&uid=&ori=pcw&ps=1&tm=1586270255962&qd_v=2&k_uid=c5c4485c6f1405f2d8a16e871c51469c&pt=0&d=0&s=&lid=&cf=&ct=&authKey=263fdbb663642b907dd4da4d7340badd&k_tag=1&ost=0&ppt=0&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a03052a3ced9e84079b662fad429d2529173d0be556e165eec7b4fe2a181c07179%22%7D&dfp=a03052a3ced9e84079b662fad429d2529173d0be556e165eec7b4fe2a181c07179&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&k_ft1=706504940322820&k_ft4=202907648&k_ft5=1&pck=&k_err_retries=1&ut=0&callback=__jp0&vf=76f3444c8b719a5bf0bfa58fc5cbbbf5"

payload = {}
headers = {
  'authority': 'cache.video.iqiyi.com',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
  'sec-fetch-dest': 'script',
  'accept': '*/*',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'no-cors',
  'referer': 'https://www.iqiyi.com/v_19rx2un304.html?vfrm=pcw_home&vfrmblk=B&vfrmrst=fcs_0_p11',
  'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
  'cookie': 'QC005=c5c4485c6f1405f2d8a16e871c51469c; QC173=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1585060178,1586270227; QYABEX={"pcw_home_movie":{"value":"new","abtest":"146_B"}}; QC007=https%253A%252F%252Fwww.baidu.com%252Fs%253Fwd%253D%2525E7%252588%2525B1%2525E5%2525A5%252587%2525E8%252589%2525BA%2526rsv_spt%253D1%2526rsv_iqid%253D0xd4a089840005f3b6%2526issp%253D1%2526f%253D8%2526rsv_bp%253D1%2526rsv_idx%253D2%2526ie%253Dutf-8%2526rqlang%253D%2526tn%253Dbaiduhome_pg%2526ch%253D%2526rsv_enter%253D1%2526rsv_dl%253Dib%2526inputT%253D5621; QC006=z6l81aod5dpln8govpp12ldo; QC008=1586270227.1586270227.1586270227.1; nu=0; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; websocket=true; QP001=1; QP0013=; QILINPUSH=1; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22hadTip%22%3A1%2C%22hideRoleTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%7D; TQC002=type%3Djspfmc140109%26pla%3D11%26uid%3Dc5c4485c6f1405f2d8a16e871c51469c%26ppuid%3D%26brs%3DCHROME%26pgtype%3Dplay%26purl%3Dhttps%3A%252F%252Fwww.iqiyi.com%252Fv_19rx2un304.html%3Fvfrm%253Dpcw_home%2526vfrmblk%253DB%2526vfrmrst%253Dfcs_0_p11%26cid%3D1%26tmplt%3D%26tm1%3D4387%2C0; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1586270254; QC010=187399980; __dfp=a03052a3ced9e84079b662fad429d2529173d0be556e165eec7b4fe2a181c07179@1586356181880@1585060182880; QP0027=2'
}

response = requests.request("GET", url, headers=headers, data = payload)

temp = response.text
json_content = re.search('try{__jp0\((.*?)\);}catch',temp,re.S)
json_data =  json.loads(json_content.group(1))
m3u8_content = json_data['data']['program']['video'][1]['m3u8']
with open('index.m3u8','a',encoding='utf-8') as f:
    f.write(m3u8_content)

# ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i index.m3u8 -acodec copy -vcodec copy out.mp4
# -protocol_whitelist "file,http,https,tcp,tls" 解决如下报错
# Protocol 'http' not on whitelist 'file,crypto'!