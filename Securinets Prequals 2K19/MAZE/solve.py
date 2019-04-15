from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from base64 import b64decode
from oldknife import *


n1 = 23489536169894875104380319731091524594886928982079989680685140526506816078328377365920912691345973867274127369888617266471562817001630072737234558761977577075038991165371860879920389022518216143091522409148685349425962144785062882226489262290433631048454159440985148197906498710065684391869085391454754106309032049154232850533299594084654876542951785594662744724164946205787746362648504615426049549895862885960678401490612936954071297209796703651121038358809482596283354654704634698014090659491829169711549185505494879482606511678080905510586288124335730218605304747220982982161819303534160762335592895244302851836981
n2 = 23260716557375690457724340517814798553284093383675955753210132374509973258283306822538580132700875733321460692101694179361245119306418651193402512612500111442624876103473535129327037097046343634997541541496318494961543987552228754832236044259856000320983983126129412431801144031562287397570846392952905862981221569085591696654562289384531854207702626277469166158114197478525681143466552721501485707709954322005798540444098755630199517759570465455471064172816576843800829708415595842816666071002921806841594943525213770657127124965423586840200929234600612382079511164305586033156711399178225762365306090386434107266037
p = 168736462866079204789584058199620418225526506348478399447895958829038354002285480486576728303147995561507709511105490546002439968559726489519296139857978907240880718150991015966920369123795034196767754935707681686046233424449917085120027639055362329862072939086970892956139024391556483288415208981014264336691
q1 = 139208418683860744636489594107518498051692876942105482068436575406002091300025595750940476658875774324613311765708231971440632450100860632595797604226237831396754383891914573698131769762436941837224713009721577421233571830899874638297795728204831707647487557389464078420524002550428515370686466308350190419191
q2 = 137852341825115687630372545540234125575043643297743715914372468140743017665122928684176567678186288631724569119078697598260381091322877334920545216266418987980787824645288016924652387350842372904949656504253960440751217710040954075691996893620788950284865727480192510130305432030965910622333944701850333681207
assert(n1 == p * q1)
assert(n2 == p * q2)

e = 65537

k1 = rsa_params(n=n1, p=p, q=q1, e=e)
k2 = rsa_params(n=n2, p=p, q=q2, e=e)

C = int(open("cipher.txt", "r").read().strip())

print(long_to_bytes(pow(C, k1['d'], k1['n'])))
print(long_to_bytes(pow(C, k2['d'], k2['n'])))

