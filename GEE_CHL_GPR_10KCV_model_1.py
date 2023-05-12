import ee

#CHL

X_train_CHL = ee.Array([[-0.265899095912738,-0.545713543775246,-0.15741445716029,0.60802567011101,0.931867424845222,0.927480730288396,0.664279470894186],[0.219761171782609,-0.0667843916334131,0.436812044329344,1.12444472911397,1.62682063030068,1.58797327067851,1.11116375082522],[0.0873083715020599,-0.18743066660044,0.291556677298545,1.01192884475019,1.53537941905654,1.54369444115515,1.03668303750338],[0.103363256384551,-0.0960319734436017,0.357581844130726,1.27158088558967,1.65973946634857,1.61749249036075,1.15585217881833],[-0.000993495351639562,-0.377539948366664,-0.0825859347504843,0.81574730278259,1.04891217523772,1.03448790163651,0.505387282474262],[-0.29800886567772,-0.275173412031005,-0.175021168315539,0.380108878707471,0.171076547293985,0.167360823470719,-0.120250709429187],[-0.145487459294057,-0.0667843916334131,-0.0165607679183027,0.331063493215569,0.174734195743751,0.207949750533799,-0.020943091666735],[-0.293995144457097,-0.344636418830202,-0.214636268414848,0.198352450119838,0.171076547293985,0.0972526767253992,-0.0755622814360836],[-0.330118635442701,-0.633456289205811,-0.381900024389707,0.00505593082822758,-0.0447247112421829,0.0013152127581197,-0.070596900547961],[-0.261885374692115,-0.242269882494543,-0.144209423793854,-0.0584145680436441,-0.231264782180226,-0.197939520096999,-0.299004421401601],[-0.61107912088629,-0.680983609647367,-0.681214114028931,-0.5257882415547,-0.739677916697639,-0.707146059615637,-0.894850127976316],[-0.595024236003799,-0.808941780066941,-0.747239280861112,-0.338261767615079,-0.54948019730983,-0.633348010410037,-0.745888701332637],[0.93420354905345,0.66074920589502,0.753732845123816,-0.222860860575312,-0.388543665520146,-0.456232692316598,-0.467827371597771],[0.552900033094293,0.331713910530402,0.251941577199235,0.163732178007907,-0.000832929844996169,0.0234546275197995,-0.0110123298904896],[1.55231661702935,1.32247574435053,1.11467042380641,-0.292101404799172,-0.534849603510768,-0.522650936601638,-0.606858036465204],[1.97375734519473,0.759459794504405,1.36116437997989,-0.863335894646019,-1.06155098027701,-1.02816757366,-1.07856922083685],[1.79313989026671,1.83430842602882,1.87175900348209,1.29466106699762,0.917236831046159,0.827853363860836,0.445802711816791],[0.970327040039055,1.11043077622666,0.727322778390943,0.336833538567558,-0.436093095367098,-0.448852887396038,-0.86505784264758],[2.17845712744649,2.58012176218862,1.85415229232684,2.58426620316702,2.19009849156457,2.18204756678359,1.96520926358231],[1.55231661702935,1.75022162832453,1.39197612450157,2.1976731645838,2.28885499970824,2.35916288487703,2.17872064177158],[1.82524966003169,1.96592254417467,1.48000968027781,2.2467185500757,1.68534300549693,1.66915112480467,1.32467512901449],[2.61193901927374,2.8323821553015,2.22829490437587,2.69966711020679,2.23764792141153,2.11193942003827,1.90562469292484],[1.72490662951612,1.88183574647038,1.34795934661345,2.37077452514345,2.10963022566973,2.09348990773687,1.69211331473557],[1.92960641176788,2.27302215318165,1.5856499472093,2.52079570429515,2.36932326560309,2.36654268979759,2.10423992844975],[1.55633033824997,1.61129561472614,1.12787545717284,2.1486277790919,1.91943250628192,1.92744429702427,1.76162864716929],[1.49612451994063,1.27494842390897,1.75291370318416,1.06385925291809,1.00502039384053,0.931170632748675,1.25515979658078],[0.801750748772901,0.989784501259637,1.10146539043997,0.662841100954899,0.942840370194518,0.949620145050075,1.51832498365128],[0.47262560868184,0.459672080949975,0.423607010962908,0.201237472795831,0.160103601944689,0.244848775136598,0.485525758921772],[0.0672397653989464,0.700964630884028,0.216728154888739,-0.0382194093116851,-0.388543665520146,-0.478372107078278,-0.433069705380912],[1.1027798403196,1.28957221481407,1.45359961354494,0.758046849262707,0.756300299256475,0.680257265449636,0.942340800629053],[0.412419790372499,0.638813519537378,0.441213722118156,0.423384218847383,0.0394012031024249,0.0197647250595196,-0.0308738534429802],[0.609092130183012,1.22010920801487,1.12787545717284,0.34548860659554,0.375904860480856,0.403514580928638,0.748690945992271],[0.825833076096638,1.49064933975911,1.29954089093652,0.483969695043261,0.745327353907178,0.827853363860836,1.3693635570076],[0.649229342389239,0.36096149234059,0.960611701197984,-0.170930452407417,-0.052040008141714,-0.194249617636719,0.276979761620622],[0.392351184269385,1.00075234443846,0.696511033869258,-0.110344976211539,-0.12153532868726,-0.205319325017559,0.0684337643194723],[1.0305328583484,1.78312515786099,1.59445330278693,0.709001463770806,0.975759206242409,1.06031721885847,1.65735564851871],[0.685352833374843,1.26763652845643,1.27313082420364,0.475314627015278,0.734354408557881,0.720846192512716,1.24026365391641],[-0.229775604927134,0.0355821447022457,-0.0429708346511754,-0.701774624790345,-0.703101432199984,-0.618588400568918,-0.512515799590874],[-0.109363968308452,-0.0521606007283191,-0.100192645905733,-0.831600645210083,-0.51656136126194,-0.434093277554918,-0.338727468506583],[-0.257871653471492,-0.0558165484545927,-0.0781842569616724,-0.782555259718182,-1.09812746477466,-1.23849201389595,-1.10339612527747],[-0.225761883706511,-0.117967659801243,-0.15741445716029,-0.794095350422158,-0.534849603510768,-0.515271131681078,-0.289073659625356],[-0.466585156943873,-0.403131582450578,-0.417113446700204,-0.964311688305815,-0.794542643444123,-0.688696547314237,-0.532377323143365],[-1.124835437126,-0.92227615958142,-1.09497182617727,-0.664269330002421,-0.831119127941778,-0.828912840804876,-0.949469317745665],[-1.20912358275907,-1.31346256629269,-1.30625236004025,-0.87776100802599,-0.765281455845998,-0.821533035884316,-0.870023223535703],[-1.124835437126,-1.05389027772727,-1.31945739340669,-1.01047205112172,-0.977425065932401,-0.969129134295516,-1.09346536350122],[-1.30946661327464,-1.44142073671226,-1.31065403782906,-0.944116529573855,-1.01400155043006,-1.0650665982628,-1.13815379149432],[-1.21715102520032,-1.25131145494604,-1.22262048205282,-0.8229455771821,-0.820146182592482,-0.854742158026836,-1.01401926929126],[-1.24524707374468,-1.3536779912817,-1.28424397109619,-0.880646030701984,-0.831119127941778,-0.828912840804876,-0.884919366200071],[-1.2131373039797,-1.07948191181118,-1.17420202637589,-0.837370690562071,-0.816488534142716,-0.891641182629636,-1.01898465017938],[-1.02449240661043,-0.896684525497505,-1.1081768595437,-0.5257882415547,-0.706759080649749,-0.769874401440397,-0.815404033766354],[-1.11279427346413,-1.03926648682217,-1.16539867079826,-0.71908476084631,-0.739677916697639,-0.718215766996477,-0.850161699983212],[-1.08469822491977,-1.07582596408491,-1.20941544868638,-0.623879012538502,-0.699443783750218,-0.784634011281517,-0.999123126626891],[-1.03251984905167,-0.936899950486514,-1.11257853733252,-0.62964905789049,-0.743335565147405,-0.795703718662357,-0.914711651528806],[-1.0365335702723,-0.87109289141359,-1.09497182617727,-0.603683853806543,-0.706759080649749,-0.692386449774517,-0.765750224885128],[-0.338146077883947,-0.761414459625384,-0.403908413333768,-0.257481132687242,-0.406831907768973,-0.504201424300238,-0.681338749787043],[-0.197665835162152,-0.479906484702322,-0.0781842569616724,-0.00359913719975479,-0.0776435472900728,-0.216389032398399,-0.413208181828422],[-0.422434223517023,-0.896684525497505,-0.456728546799513,-0.430582493246892,-0.553137845759596,-0.570619668585278,-0.65651184534643],[0.516776542108689,0.170852210574366,0.824159689744809,0.619565760814987,0.335670727533435,0.237468970216038,-0.169904518310414],[-1.24123335252405,-0.991739166380617,-1.01574162597865,-1.18357341168137,-1.06155098027701,-1.07244640318336,-0.914711651528806],[1.31149334379198,0.404832865055872,0.788946267434312,-1.28743422801716,-1.38708169230614,-1.35287899016463,-1.16794607682306],[-1.22517846764156,-0.765070407351658,-1.04215169271152,-1.18068838900538,-1.38708169230614,-1.37870830738659,-1.16794607682306],[-1.24123335252405,-0.988083218654343,-1.06416008165558,-1.28166418266517,-1.0944698163249,-1.10565552532588,-0.944503936857542],[-0.310050029339588,0.11235704695399,-0.0913892903281085,0.558980284619109,0.606336712816087,0.650738045767397,0.609660281124838],[0.496707936005576,0.60956593772719,0.709716067235695,0.962883459258294,0.887975643448035,1.04555760901735,1.02675227572714],[-0.0411307075578664,0.214723583289649,0.185916410367054,0.991733686018235,0.763615596156006,0.883201900765035,0.535179567802998],[-0.394338174972664,0.00267861516578396,-0.201431235048411,0.391648969411447,0.500264907772885,0.621218826085157,0.535179567802998],[0.950258433935941,0.499887505938984,0.912193245521051,1.09270947967803,1.39638877796545,1.30016087877667,1.48356731743442],[0.484666772343708,0.689996787705208,0.692109356080446,0.331063493215569,0.203995383341875,0.196880043152959,0.227325952739396],[0.251870941547591,0.141604628764178,0.163908021422994,0.792667121374637,0.887975643448035,0.894271608145875,0.609660281124838],[1.33557567111572,0.956880971723176,1.53282981374356,1.49661265431722,2.03281960822466,2.10455961511771,2.27306287864592],[1.7730712841636,1.26398058073015,1.62966672509742,1.36390161122148,1.58292884890349,1.46989639194955,1.94534774002982],[0.380310020607517,-0.216678248410628,0.062669432280315,0.359913719975511,0.522210798471479,0.628598631005717,0.723864041551658],[0.283980711312572,0.159884367395546,0.190318088155866,0.466659558987295,0.386877805830153,0.344476141564158,0.510352663362385],[-0.426447944737646,-0.999051061833164,-0.760444314227548,-0.168045429731423,-0.249553024429054,-0.216389032398399,-0.443000467157158],[0.597050966521143,0.258594956004931,0.419205333174096,0.610910692787004,0.697777924060226,0.842612973701956,1.20054060681143],[1.10679356154023,0.646125414989925,1.18069559063859,0.833057438838556,1.2098487070274,1.21529312219023,1.61763260141373],[1.38374032576319,0.85817038311379,1.38317276892395,0.755161826586713,0.580733173667728,0.388754971087518,0.535179567802998],[0.777668421449165,0.148916524216725,0.714117745024507,0.284903130399662,0.500264907772885,0.481002532594517,0.828137040202233],[-0.289981423236474,-0.150871189337705,-0.0693809013840479,-0.626764035214496,-0.260525969778351,-0.07248283644748,0.351460474942462],[-0.0732404773228481,-0.0887200779910544,0.141899632478933,-0.678694443382392,-0.527534306611237,-0.581689375966118,-0.323831325842215],[-0.591010514783177,-0.271517464304731,-0.425916802277829,-0.903726212109937,-0.688470838400921,-0.566929766124998,-0.373485134723441],[-0.35821468398706,-0.150871189337705,-0.104594323694545,-0.771015169014205,-0.169084758534212,0.0197647250595196,0.281945142508745],[-0.189638392720906,0.137948681037904,0.00104594323694563,-0.485397924090782,-0.198345946132336,-0.0909323487488799,0.202499048298783],[-1.28137056473028,-0.651736027837178,-0.954118136935281,-1.20665359308933,-1.21517221516716,-1.14624445238896,-1.16794607682306],[-0.306036308118965,-0.432379164260767,-0.148611101582666,-1.34801970421304,-1.40536993455497,-1.34180928278379,-1.16794607682306],[-1.43790569233457,-0.907652368676326,-1.30185068225144,-1.3191694774531,-1.39439698920567,-1.40084772214827,-1.16794607682306],[-1.2492607949653,-1.10872949362137,-1.25783390436332,-1.6653721985724,-1.41634287990427,-1.35656889262491,-1.16794607682306],[-0.607065399665668,-0.472594589249776,-0.566770491519816,-0.0872647948035858,-0.0849588441896042,0.0013152127581197,-0.159973756534168],[-0.578969351121309,-0.282485307483552,-0.500745324687634,-0.407502311838939,-0.191030649232805,-0.1610404954942,-0.194731422751027],[-0.755573084828708,-0.878404786866138,-0.813264447693294,-0.341146790291073,-0.278814212027179,-0.268047666842319,-0.224523708079762],[-0.627134005768781,-0.640768184658358,-0.610787269407937,-0.309411540855137,-0.110562383337963,-0.18317991025588,-0.085493043212329],[-1.35763126792211,-1.41948505035462,-1.53513960505848,-1.07971259534558,-1.04326273802818,-1.05030698842168,-1.04381155461999],[-1.28137056473028,-1.26959119357741,-1.45150772707105,-0.984506847037774,-0.999370956630994,-1.01340796381888,-1.10836150616559],[0.0431574380752103,0.0867654128700751,-0.100192645905733,-0.851795803942042,-1.04326273802818,-1.06875650072308,-1.16794607682306],[-1.40178220134896,-1.45238857989108,-1.5439429606361,-0.987391869713768,-1.1054427616742,-1.14624445238896,-1.16794607682306],[-1.33354894059838,-1.27324714130368,-1.50872953832561,-0.903726212109937,-0.984740362831932,-0.895331085089916,-0.954434698633787],[-0.875984721447389,-0.852813152782223,-1.15219363743183,-0.765245123662217,-0.838434424841309,-0.817843133424036,-0.879953985311948],[-0.95224542463922,-1.1050735458951,-1.2534322265745,-1.01624209647371,-0.951821526784042,-0.950679621994116,-1.02891541195563],[-0.851902394123653,-1.05389027772727,-1.288645648885,-1.13164300351348,-1.1054427616742,-1.09458581794504,-1.04877693550812],[-0.835847509241162,-1.04657838227472,-1.30185068225144,-0.975851779009791,-0.988398011281698,-1.01340796381888,-1.15304993415869],[-0.904080769991748,-0.991739166380617,-1.2534322265745,-0.871990962674001,-0.801857940343654,-0.884261377709076,-0.954434698633787]]);

alpha_coefficients_CHL = ee.Image([[-0.0215248915934536,-0.0111968491665146,0.0116960792744666,-0.0162212549001678,0.00118007019134313,0.0118723198331496,0.0651382042500617,0.0363354701787446,-0.0399515728802492,-0.0790198989411808,-0.0226190024820923,-0.114135045936762,-0.000916499108182643,0.00635081222158293,-0.00087070349632855,-0.00969176442816368,-0.0309033374952366,-0.00868204129243531,-0.0092424576853593,0.0586112548232299,0.00541740863090046,0.0293997287331683,0.0246667628923343,-0.0316346400620375,0.00172311026143524,0.0326036822860897,-0.0335830279917369,0.0975189891679264,0.0303017299397233,0.0148702165434357,0.0563958108814236,0.0139207855535941,-0.02355513651969,-0.000287226468055397,0.0195531102349553,-0.00159905109441766,-0.010455602294781,-0.0113925455040646,-0.00949796427484009,0.0100000541471092,-0.0327970823999052,-0.0145768223693352,-0.0757043761250079,-0.0223223542902328,-0.046815133537737,-0.0685129950117778,0.0116165688871376,-0.0227656484896158,0.00811675199694142,0.0483568517200885,0.00664308314440734,0.0291622855548524,0.0679030953585738,-0.0369033261532733,-0.00216136509307829,-0.00834216145573206,0.0770083132614246,0.0107210091419488,-0.049787232005731,-0.017126680855222,0.0483695178767216,-0.0274818881576195,-0.00442248544935997,0.0378652129634258,0.0729232496515899,-0.0720054944208321,-0.0130081205497903,-0.174170748389842,0.0287816722978304,-0.0455137245071721,-0.0409300742699122,0.0309872226488284,-0.156611612138272,-0.0783185040857914,-0.0444607117900905,0.0590253463420725,-0.00529512519826345,0.067533871227266,-0.0360415259260588,0.00206140319816751,0.0470329977478838,-0.0134429107116891,0.0216748121632559,-0.0190676895392694,-0.0121333581320296,-0.0488342222849444,0.00705188527567056,0.115731533502367,-0.0162231389745252,0.0101660168259668,0.101196710366061,0.0120821455224181,0.0678632339571166,0.0144365345234686,0.100196052329464,-0.022118871944819,0.0300749551711651,0.0310393234681185,-0.0497447061532432,0.0467251439868063,0.0133765080670541]]);

mx_CHL       =  ee.Image([[0.0464247524752475,0.0897267326732673,0.0474762376237624,0.0912247524752475,0.0388227722772277,0.0380643564356436,0.0236217821782178]]);

sx_CHL       =  ee.Image([[0.0249145355402849,0.0273526886835247,0.02271860976607,0.0346617726203972,0.0273399703042564,0.0271009873774312,0.0201394419185855]]);

mean_model_CHL = 99.5425742574258;

hyp_ell_CHL  = ee.Image([1.21770905212314,0.4295697570492,0.648418027583889,0.39965202343608,0.356735239435395,0.54086088154403,0.393117680356952]);

hyp_sign_CHL = ee.Array([273.873075578615]);

hyp_sig_CHL  =3883.4372334944;

XDX_pre_calc_CHL =  ee.Image([[1.32634914381911],[3.48311604540446],[3.04105551167926],[3.66904447941552],[1.40330418934991],[0.249551030456733],[0.106124400296192],[0.219668545308401],[0.40233021955694],[0.198993737896597],[1.84573776802878],[1.66339777306007],[1.89098176399777],[0.471736564459114],[4.91991171315514],[7.92194606946086],[9.05125812793971],[2.53554369003502],[19.3412915284725],[14.1819749856298],[12.3646865358167],[23.512157695966],[13.6524244774282],[17.6956470106399],[11.2782485836527],[7.31731486642229],[3.87696882715769],[0.629552718516438],[0.498970346070493],[4.59841087422696],[0.581426590612171],[2.32263674173126],[4.27966133999297],[1.23078688374459],[0.967012359811095],[6.53594751542994],[3.48166757294901],[0.749431138129914],[0.540838249300499],[2.06942250586934],[0.61462603676505],[1.41251602339603],[3.83231284261876],[4.80718979079915],[4.87360063281618],[5.94018917029429],[4.75582702809245],[4.9806461147396],[4.54291499443329],[3.29040173572243],[3.81748308915037],[3.93382370614693],[3.5048186481926],[3.22533804119851],[0.899595162406051],[0.24507846432584],[1.2267422528785],[1.01362373058386],[4.88041025796836],[5.44343226287127],[5.59135350347697],[5.12545872603518],[0.759073792246802],[2.44417124435969],[1.17985767643444],[0.687570599965582],[4.69878180292903],[0.901088787794998],[1.21433440043524],[10.8849774206495],[10.5301794121896],[0.767591369237406],[0.439668436809232],[1.16114579543205],[1.85020716575316],[5.20196217584417],[4.43103906843716],[1.59308567957443],[0.347906164554032],[0.53056838692544],[1.29880084438391],[0.452364536871835],[0.180756657189873],[5.12765973182704],[3.14952863661132],[6.95726040142996],[6.81000213621938],[0.768673213034769],[0.713367281845535],[1.58841733425277],[0.960838814100348],[6.51723084673915],[5.83995590796534],[1.8442949640948],[6.91705647319281],[5.8018957253214],[3.25861143347299],[4.28842899069376],[4.46577269267331],[4.22741946320011],[3.7508083523743]]);

veg_index_CHL = 'Chl' ;
model_CHL = '2023_02_15_Chl_GPR_MLRA_10KCV_model' ;

scaleFactor_CHL = 10000;  

units_CHL = 'mug L-1'

CHL_model = {
  
  'X_train': X_train_CHL,
  'alpha_coefficients' : alpha_coefficients_CHL,
  'mx': mx_CHL,
  'sx': sx_CHL,
  'mean_model': mean_model_CHL,
  'hyp_ell': hyp_ell_CHL,
  'hyp_sign': hyp_sign_CHL,
  'hyp_sig': hyp_sig_CHL,
  'XDX_pre_calc': XDX_pre_calc_CHL,
  'veg_index': veg_index_CHL,
  'model': model_CHL,
  'scaleFactor' : scaleFactor_CHL,
  'units': units_CHL
};

models = {
  'Chl' : CHL_model

};