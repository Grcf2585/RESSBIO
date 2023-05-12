import ee

#ZSD

X_train_ZSD = ee.Array([[-0.298624815496939,-0.6117773492097,-0.210191552349736,0.580606474759916,0.871300981041615,0.862833765610397,0.595379029903919],[0.186389985511512,-0.116522589355103,0.4025519447315,1.08925874735154,1.54762818581882,1.50537591308788,1.03114875263348],[0.0701467687408917,-0.146767154842407,0.320852811787335,1.23418202054804,1.57966473762406,1.53409288057291,1.07472572490644],[-0.0340712876741475,-0.437871097657704,-0.133031260124692,0.785204036919677,0.985208720793566,0.966932772743621,0.44043868404452],[-0.326683522993295,-0.403845961484488,-0.2691964816983,0.177094616055944,0.130900672653935,0.0551690550940036,-0.126061955503908],[-0.36275900406004,-0.702511045671611,-0.44167242902487,-0.0132947820649448,-0.0791167225137246,-0.0381610892323352,-0.121220069695802],[-0.294616428711745,-0.297989982278925,-0.196575030192376,-0.0758107038359827,-0.260657182743396,-0.23200061975627,-0.343946816868688],[-0.643346079023606,-0.75165846458848,-0.750313597925049,-0.536155218695445,-0.755443927290933,-0.727368308872991,-0.924973113841435],[-0.627312531882831,-0.883978438595433,-0.818396208711853,-0.351449086190105,-0.570343850194013,-0.655575890160423,-0.779716539598249],[0.89988283327601,0.635810977141576,0.72934847650816,-0.237783773879127,-0.41372070803508,-0.483274085250259,-0.5085709343443],[0.747564135438645,0.684958396058444,0.752042680103762,0.663013826185376,0.550935462989254,0.521819776725697,0.416229255003989],[0.519086088682598,0.295559615409409,0.211920634528449,0.14299502236265,-0.0364013201067431,-0.0166233636185648,-0.0631174399985272],[1.51717439819586,1.32009427129182,1.10153341547602,-0.305982961265713,-0.556105382725019,-0.54788726209157,-0.644143736971274],[1.93805501064121,0.737886385661225,1.35570849574676,-0.868626257205056,-1.0686902116088,-1.03966533027266,-1.10412288874137],[1.75767760530748,1.84937416731963,1.88221401916471,1.25691508301024,0.857062513572621,0.76591400034843,0.382336054347245],[2.14248273668609,2.62061058724588,1.86405865628823,2.52712494808542,2.09580918337509,2.08330488372406,1.86395311162775],[1.51717439819586,1.76242104154364,1.3874803807806,2.14634615184364,2.1919188387908,2.25560668863422,2.07215420137632],[2.57538850948702,2.88146996457387,2.24986011741345,2.6407902603964,2.14208420264932,2.01510208594712,1.80585048193048],[1.68953502995919,1.8985215862365,1.3420919735894,2.31684412031011,2.01749761229562,1.99715398126898,1.59764939218191],[1.89396275600407,2.30304264962919,1.58718937242189,2.46460902631438,2.27023040987026,2.26278593050548,1.99952591425473],[1.52118278498105,1.61875935547894,1.11514993763338,2.09803839411148,1.8323975351987,1.8356210391657,1.6654357934954],[1.46105698320314,1.27094685237495,1.75966531974846,1.02958445838828,0.942493318386585,0.866423386546025,1.17156344106856],[0.767606069364614,0.976062338873741,1.08791689331866,0.634597498107631,0.881979831643361,0.884371491224167,1.42818338889819],[0.438918352978722,0.427879589416363,0.388935422574139,0.179936248863718,0.120221822052189,0.19875389251914,0.421071140812095],[0.0340712876741472,0.677397254686618,0.175609908775487,-0.0559192741815617,-0.41372070803508,-0.504811810864029,-0.474677733687556],[1.06823507825415,1.2860691351186,1.45102415084828,0.728371380764188,0.700439371413689,0.622329162923293,0.866524635157868],[0.575203503675311,1.21423829208626,1.11514993763338,0.322017889252441,0.330239217219849,0.353107592751162,0.677691088641725],[0.791656390075777,1.49400052284382,1.29216472567907,0.458416264025615,0.689760520811944,0.76591400034843,1.282926814655],[0.358750617274846,0.98740405093148,0.670343547159596,-0.126960094375923,-0.153868676725943,-0.239179861627526,0.0143527329311724],[0.651362852593994,1.26338571100313,1.26493168136435,0.449891365602292,0.679081670210198,0.661814993215206,1.15703778364424],[-0.262549334430194,-0.0106666101495401,-0.0921816936526095,-0.709494819969686,-0.719847758618448,-0.641217406417909,-0.552147906617256],[-0.14229773087438,-0.101400306611451,-0.151186623001173,-0.837368296319537,-0.538307298388777,-0.461736359636488,-0.382681903333538],[-0.290608041926551,-0.105180877297364,-0.128492419405572,-0.789060538587371,-1.10428638028128,-1.24427372360348,-1.1283323177819],[-0.483010607615854,-0.184572861701536,-0.43713358830575,-1.02775769444043,-1.15412101642276,-1.16530206301966,-1.19127683328728],[-0.499044154756629,-0.464335092459095,-0.477983154777833,-0.968083405477162,-0.80883818029966,-0.709420204194849,-0.571515449849681],[-1.15641958752841,-1.00117612985873,-1.17696462552235,-0.672553593468618,-0.844434348972145,-0.845825799748729,-0.978233857730604],[-1.24059571001748,-1.40569719325142,-1.39482898004013,-0.882834421243928,-0.780361245361672,-0.838646557877472,-0.900763684800904],[-1.15641958752841,-1.1372766745516,-1.40844550219749,-1.01354953040155,-0.986819023662083,-0.982231395302608,-1.11864854616568],[-1.34080537964733,-1.53801716725837,-1.39936782075925,-0.94819197582274,-1.02241519233457,-1.07556153962895,-1.16222551843864],[-1.27667119108423,-1.44728347079646,-1.37213477644453,-0.885676054051703,-0.844434348972145,-0.845825799748729,-0.915289342225223],[-1.24460409680268,-1.16374066935299,-1.25866375846652,-0.843051561935086,-0.830195881503151,-0.906849355654412,-1.04602025904409],[-1.05620991789857,-0.974712135057344,-1.19058114767972,-0.536155218695445,-0.723407375485697,-0.788391864778674,-0.847502940911736],[-1.14439442717283,-1.12215439180795,-1.24958607702828,-0.726544616816333,-0.755443927290933,-0.738137171679876,-0.881396141568479],[-1.11633571967648,-1.15996009866708,-1.29497448421948,-0.632770734159776,-0.7162881417512,-0.802750348521188,-1.02665271581167],[-1.06422669146896,-1.01629841260239,-1.19511998839884,-0.638453999775325,-0.759003544158181,-0.813519211328073,-0.94434065707386],[-1.06823507825415,-0.948248140255953,-1.17696462552235,-0.612879304505355,-0.723407375485697,-0.713009825130477,-0.799084082830674],[-0.230482240148644,-0.543727076863267,-0.128492419405572,-0.021819680488268,-0.111153274318961,-0.249948724434412,-0.455310190455132],[-0.454951900119497,-0.974712135057344,-0.518832721249915,-0.442381336038887,-0.573903467061261,-0.59455233425474,-0.692562595052337],[0.483010607615854,0.129214505229239,0.801969928014084,0.591973005991014,0.291083431680116,0.191574650647883,-0.218057785857927],[-1.27266280429903,-1.07300697289108,-1.09526549257819,-1.18404749886802,-1.0686902116088,-1.0827407815002,-0.94434065707386],[1.27667119108423,0.371171029127668,0.765659202261122,-1.2863462799479,-1.38549611279391,-1.35555197260796,-1.19127683328728],[-1.25662925715826,-0.838611590364478,-1.12249853689291,-1.18120586606025,-1.38549611279391,-1.38067931915736,-1.19127683328728],[-1.18046990823958,-0.774341888703958,-0.977255633881063,-0.999341366362681,-1.04021327667081,-1.08992002337146,-1.08959723131705],[-0.342717070134071,0.0687253742546317,-0.142108941562932,0.532298717027751,0.554495079856502,0.593612195438266,0.542118286014751],[0.462968673689885,0.582882987538794,0.683960069316958,0.930127310116175,0.828585578634634,0.977701635550506,0.948836693895674],[-0.0741551555260853,0.174581353460195,0.143838023741645,0.958543638193919,0.707558605148186,0.819758314382856,0.469489998893158],[-0.426893192623141,-0.0446917463227566,-0.255579959540939,0.367484014176832,0.451266190706296,0.564895227953238,0.469489998893158],[-0.531111249038179,-0.294209411593012,-0.387206340395427,0.296443193982471,0.533137378653011,0.532588639532583,0.469489998893158],[0.218457079793062,0.0989699397419357,0.121143820146044,0.762470974457482,0.828585578634634,0.830527177189741,0.542118286014751],[1.30072151179539,0.942037202700525,1.53272328379245,1.45582937955445,1.9427456580834,2.00792284407586,2.16415003173034],[1.73763567138152,1.25960514031721,1.63257777961309,1.32511427039682,1.50491278341184,1.39050804314777,1.84458556839533],[0.346725456919264,-0.271525987477534,0.0167504836062771,0.336226053291313,0.472623891909787,0.572074469824495,0.653481659601194],[0.250524174074613,0.1178727931715,0.148376864460765,0.441366467178968,0.340918067821594,0.295673657781107,0.445280569852626],[0.56317834331973,0.21994820169115,0.384396581855019,0.583448107567691,0.643485501537714,0.780272484090943,1.11830269717939],[1.07224346503934,0.620688694397923,1.16961602626283,0.802253833766324,1.1418318629525,1.14282419858941,1.52502110506031],[0.743555748653451,0.106531081113761,0.688498910036078,0.262343600289177,0.451266190706296,0.428489632399359,0.755161261571425],[1.15641958752841,0.25775390855028,1.1196887783525,0.765312607265256,1.21302420029747,1.1535930613963,1.53954676248463],[-0.322675136208102,-0.203475715131101,-0.119414737967331,-0.63561236696755,-0.289134117681384,-0.109953507944904,0.290340223993227],[-0.106222249807636,-0.139206013470581,0.0984496165504421,-0.686761757507491,-0.548986148990522,-0.605321197061625,-0.368156245909219],[-0.623304145097637,-0.328234547766229,-0.487060836216073,-0.908409116513898,-0.705609291149454,-0.590962713319111,-0.416575103990282],[-0.390817711556396,-0.203475715131101,-0.155725463720293,-0.777694007356273,-0.200143696000172,-0.0202129845541931,0.22255382267974],[-0.222465466578256,0.0951893690560226,-0.0467932864614067,-0.496372359386602,-0.22862063093816,-0.127901612623046,0.14508364975004],[-1.31274667215097,-0.721413899101176,-1.03172172251051,-1.20678056133022,-1.21819412003323,-1.15453320021277,-1.19127683328728],[-0.338708683348877,-0.494579657946399,-0.201113870911496,-1.34602056891116,-1.40329419713015,-1.34478310980108,-1.19127683328728],[-1.46907375677353,-0.986053847115083,-1.39029013932101,-1.31760424083342,-1.39261534652841,-1.40221704477113,-1.19127683328728],[-1.28067957786942,-1.1939852348403,-1.3449017321298,-1.65860017776635,-1.4139730477319,-1.35914159354359,-1.19127683328728],[-0.639337692238412,-0.536165935491441,-0.632303739227922,-0.104227031913727,-0.118272508053458,-0.0381610892323352,-0.208374014241714],[-0.611278984742056,-0.339576259823967,-0.564221128441118,-0.419648273576692,-0.221501397203663,-0.196104410399985,-0.242267214898458],[-0.787648003290583,-0.95580928162778,-0.886478819498657,-0.354290718997879,-0.306932202017626,-0.300203417533209,-0.271318529747095],[-0.607270597956862,-0.672266480184308,-0.691308668576485,-0.158218055261442,-0.104034040584464,-0.127901612623046,-0.135745727120121],[-1.31274667215097,-1.36033034502047,-1.5446107237711,-0.987974835131583,-1.00817672486557,-1.02530684653015,-1.13317420359],[0.0100209669629845,0.0422613794532413,-0.151186623001173,-0.857259725973958,-1.05089212727256,-1.07915116056458,-1.19127683328728],[-0.883849286135235,-1.1372766745516,-1.37667361716365,-1.13289810832808,-1.11140561401578,-1.10427850711397,-1.07507157389273],[-0.935958314342754,-1.07300697289108,-1.34036289141068,-0.877151155628379,-0.815957414034157,-0.899670113783155,-0.98307574353871]]);

alpha_coefficients_ZSD = ee.Image([[4.57244924604778,7.48767748940629,-10.068479982813,-12.7601052074649,-7.4437874077316,5.70907832960806,9.17775845870278,6.92739204233031,-25.5989817702877,-25.5100475559557,7.87188489729678,5.5012474433853,-34.4813494836243,-4.84498078133772,24.8775712502562,-3.71757669741366,6.33938333768195,1.02856742616251,-1.68229759158881,-0.284643218056865,5.54976683038404,-12.4581720312537,8.34690529575559,-24.6753600595469,-27.4819052179096,-27.3721204440034,15.7918927636382,-8.83109639970828,5.80844170503607,9.72560920039377,-15.1626417484413,-40.4635357274636,8.11239002843438,-35.4984368772383,-30.1457775444982,-11.3873936506207,5.00656593263733,19.837334644227,-45.0240235761077,-9.68493323647789,-19.745583590945,-7.06417595647453,1.24223961974455,17.779095067418,-8.67629304225839,-7.64598769930084,10.330997180932,-3.38590655296667,-0.8417817228696,11.8750487457196,35.5723015498329,-5.40476455326071,11.3146750505638,0.923606655449069,-8.09321337665675,4.79610862318454,-3.31068258857695,-3.11810471980112,-1.19761702099048,-32.8582286816693,12.6792989968992,-2.68163483234812,76.9504059482635,-14.5036520676221,13.5589051148427,-4.87177354812398,3.94616460961734,27.3027810208496,63.4472161695801,10.9619478042617,-13.295594418097,34.3247631046685,22.0272904882879,31.6002008520537,8.13239966873165,-25.384208837025,6.14955228836854,-14.3997227533956,-9.95923603114794,4.82049860851369,-19.9396754346559,-9.66043430605161,56.7450753296568,8.17694489098015]]);

mx_ZSD       =  ee.Image([[0.04725,0.0909821428571429,0.0485309523809524,0.0918678571428571,0.039822619047619,0.0391630952380952,0.0247035714285714]]);

sx_ZSD       =  ee.Image([[0.024947692265971,0.0264510330074284,0.0220320575645541,0.035191035142334,0.0280929110433446,0.0278580947106309,0.0206531099582277]]);

mean_model_ZSD = 0.328095238095238;

hyp_ell_ZSD  = ee.Image([0.000123749577440482,3.50412469281498e-05,0.0283066683111066,0.103461564741037,4.56454582482965e-05,6.88107913608674e-05,5.17461959796617e-05]);

hyp_sign_ZSD = ee.Array([0.00217712682015361]);

hyp_sig_ZSD  =0.0757114252535376;

XDX_pre_calc_ZSD =  ee.Image([[0.0362562713718473],[0.127667655041759],[0.160844248313425],[0.0644152423700646],[0.00531684142271929],[0.00557492173356414],[0.00171521919293173],[0.0458548756843176],[0.0318901911382997],[0.0210591871041644],[0.0616168990900326],[0.00342349184300281],[0.0444354322618177],[0.13076254473459],[0.264318750442842],[0.76058806153179],[0.532305418866326],[0.866571515773599],[0.60741569925458],[0.701189878760852],[0.491521354148798],[0.197807214664228],[0.0754693203067655],[0.00767456021546644],[0.00124969615104726],[0.114774874621273],[0.0460594543449026],[0.0693083527924701],[0.014442699535122],[0.0664618958798059],[0.0523975722297152],[0.0732311240807727],[0.0651231472799323],[0.114951730685187],[0.103549610412045],[0.0863421987998016],[0.13608745174726],[0.162823143151737],[0.148952536246111],[0.134852247894248],[0.118762067281615],[0.0701407144635195],[0.0991237689436082],[0.0892186747998631],[0.0828984448588002],[0.0783386653385919],[0.000549133156271385],[0.0279904384975277],[0.0545001532697579],[0.179426440571023],[0.188284835379222],[0.180533241610723],[0.130745023966389],[0.0299548405372913],[0.102932437607842],[0.0957289915546999],[0.0158862195607931],[0.0134178760170684],[0.060664303423317],[0.286712197961345],[0.25795882499962],[0.0117763346631923],[0.0208077891119646],[0.0395685935665757],[0.105738094973784],[0.020659141107168],[0.0965351467192903],[0.0422257859836216],[0.0491192060311034],[0.0921999519755407],[0.0632855991150017],[0.025564454590363],[0.181268489782753],[0.188904145371379],[0.234930197930909],[0.336362778854072],[0.0125048062522814],[0.0272895691429773],[0.0353544351272099],[0.0161819684338591],[0.168986202116697],[0.0768843790529205],[0.186778333415958],[0.130742556497639]]);

veg_index_ZSD = 'ZSD' ;
model_ZSD = 'ZSD_Chl_GPR_MLRA_4KCV_model_20230216' ;

scaleFactor_ZSD = 10000;  

units_ZSD = 'm'

ZSD_model = {
  
  'X_train': X_train_ZSD,
  'alpha_coefficients' : alpha_coefficients_ZSD,
  'mx': mx_ZSD,
  'sx': sx_ZSD,
  'mean_model': mean_model_ZSD,
  'hyp_ell': hyp_ell_ZSD,
  'hyp_sign': hyp_sign_ZSD,
  'hyp_sig': hyp_sig_ZSD,
  'XDX_pre_calc': XDX_pre_calc_ZSD,
  'veg_index': veg_index_ZSD,
  'model': model_ZSD,
  'scaleFactor' : scaleFactor_ZSD,
  'units': units_ZSD
};

models = {
  'ZSD' : ZSD_model

};