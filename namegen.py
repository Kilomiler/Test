import random

prefix = ["acorn","adder","alder","amber","ant","apple","arch","argus","ash","ashen","aspen","asphodel","aster",
          "auburn","avocet","badger","barbel","bark","barley","basil","bass","bat","bay","beam","bean","bear","beaver",
          "bee","beech","beetle","bellow","berry","birch","bird","bittern","black","blaze","blazing","bleak",
          "blizzard","blood","bloom","blooming","blossom","blue","blurry","boar","bone","borage","boulder","bounce",
          "bracken","bramble","brambling","branch","brave","bream","breeze","briar","bright","brindle","bristle",
          "broken","brook","broom","brown","brush","bubble","buck","bug","bumble","burdock","burnet","burning","burnt",
          "burr","bush","buzzard","campion","cardinal","carp","cedar","celandine","chamomille","chanterelle","cheetah",
          "cherry","chervil","chestnut","chill","chive","chub","cinder","cinnamon","claw","clear","cliff","cloud",
          "clouded","cloudy","clover","coal","cold","comfrey","comma","cone","condor","coot","copper","cormorant",
          "coyote","crag","crake","crane","cream","creek","cricket","crimson","crisp","crooked","crouch","crow",
          "cuckoo","curl","curlew","curly","current","cypress","dace","daffodil","daisy","damp","dandelion","dapple",
          "dappled","dark","dawn","day","deep","deer","dew","dewy","dipper","dirt","diver","dock","doe","dog","dove",
          "down","dream","drift","drifting","drizzle","dry","duck","dunlin","dunnock","dusk","dust","dusty","eagle",
          "ebony","echo","eel","egg","egret","elder","elk","elm","ember","evening","faded","fading","falcon","fallen",
          "falling","fallow","fang","fawn","feather","fennel","fern","ferret","fidget","fin","finch","fir","fire",
          "fish","flail","flame","flare","flash","flax","flaxen","fleck","flecked","fleet","flicker","flickering",
          "flight","flint","flip","flower","flurry","flutter","fly","foam","fog","foggy","forest","fox","freckle",
          "freckled","fringe","fritillary","frog","frond","frost","frosted","frozen","fumitory","furl","furled",
          "furze","fuzz","fuzzy","gadwall","gale","gannet","garlic","gentle","gill","ginger","glade","gliding",
          "godwit","gold","golden","goose","gorse","grass","gravel","gray","grebe","green","grouse","gudgeon",
          "gull","gust","hail","half","hard","hare","harrier","haven","hawk","hawthorn","hay","haze","hazel",
          "heather","heavy","hedge","hemlock","heron","herring","hickory","hill","hollow","holly","honey","hoopoe",
          "hoot","hop","hope","hopping","hornet","horse","hound","ice","iris","ivy","jackdaw","jagged","jaguar",
          "jasmine","jay","jump","juniper","kestrel","kink","kite","knot","lake","laburnum","lamprey","lapping",
          "larch","lark","laurel","lavender","leaf","leech","leopard","lichen","light","lightning","lilac","lily",
          "limpet","linden","linnet","lion","little","lizard","loach","log","lone","long","loon","lost","loud","lynx",
          "maggot","magpie","mahogany","maize","mallard","mallow","maple","marigold","marked","marsh","marten",
          "martin","meadow","melting","midge","milk","mink","minnow","mint","miracle","mist","misted","mistle","misty",
          "mole","moon","moor","moose","morning","mosquito","moss","mossy","moth","mottle","mottled","mountain",
          "mouse","mud","muddy","mumble","muntjac","murk","murky","murmur","myrtle","nectar","needle","nerite",
          "nettle","newt","night","nightingale","nut","oak","oat","odd","oleander","olive","one","orange","orchid",
          "osprey","otter","owl","pad","pale","pansy","panther","parsley","partridge","patch","patched","patchy",
          "pear","peat","pebble","pelican","peony","perch","peregrine","petal","petrel","pheasant","pigeon","pike",
          "pine","pipit","plover","plum","pochard","pod","pollen","pond","pool","poplar","poppy","possum","pounce",
          "pouncing","prickle","primrose","privet","puddle","puma","quail","quick","quiet","quill","rabbit","raccoon",
          "radiant","ragged","raggedy","rail","rain","rapid","rat","raven","red","reed","ridge","ripped","ripple",
          "rippled","rising","roach","roaring","robin","rock","rook","root","rose","rowan","rubble","rudd","ruddy",
          "running","rush","rushing","russet","rye","sable","sage","salamander","salmon","sand","sandy","sap","scale",
          "scar","scarlet","scarred","scorch","scratch","sedge","seed","serpent","shade","shaded","shallow","sharp",
          "shattered","sheep","shell","shimmer","shimmering","shine","shining","shiver","shivering","short","shred",
          "shrew","shrike","shy","silent","silk","silver","skink","skipper","skunk","slate","sleek","sleet","slight",
          "sloe","slug","small","smoke","smudge","smudged","snail","snake","snap","sneeze","sneezing","snow","soar",
          "soaring","soft","soot","sorrel","spark","sparrow","speckle","speckled","spider","spike","spire","spirit",
          "splash","splinter","split","splotch","splotched","spot","spotted","spruce","squirrel","stag","starling",
          "stem","stick","still","stoat","stone","stork","storm","straw","stream","strike","stripe","stump","stumpy",
          "summit","sun","sunny","swallow","swamp","swan","sweet","swift","swirl","swirled","swoop","sycamore","tall",
          "talon","tangle","tansy","tawny","teasel","tench","tern","thaw","thin","thistle","thorn","thrift","thrush",
          "thyme","tiger","timber","tiny","tip","toad","tormentil","torn","torrent","tree","trout","truffle","tuft",
          "tulip","tumble","tunnel","turtle","twig","twilight","twisted","twitch","twite","valerian","venom",
          "vervain","vine","violet","viper","vixen","vole","vulture","wandering","warbler","warm","wasp","water",
          "wave","wax","weasel","web","weed","wet","wheat","whimbrel","whinchat","whisker","whisper","whispering",
          "whistle","white","whorl","wigeon","wild","willow","wing","winged","wish","wisp","wisteria","wolf","wood",
          "woolly","worm","wren","yarrow","yellow","yew"]
suffix = ["acorn","adder","ant","ash","aspen","bark","beam","bean","bear","bee","belly","beech","berry","bird","birch",
          "bite","bittern","blaze","blizzard","blood","bloom","blossom","boar","bracken","bramble","branch","breeze",
          "briar","bright","bristle","brook","brush","bumble","burn","burnet","burr","burrow","bush","buzzard","call",
          "caller","cardinal","chase","chaser","cherry","chirp","claw","cloud","clover","crawl","creek","crow","cry",
          "dace","dance","dapple","dapples","daisy","dawn","deer","dew","doe","dog","dove","dream","drop","dusk",
          "dust","eagle","ear","ears","echo","elm","ember","eye","eyes","face","fall","falcon","fang","fawn","feather",
          "fern","fin","finch","fire","flake","flame","flicker","flight","flower","fluff","fly","fog","foot","fox",
          "freckle","frog","frost","fur","fury","furze","fuzz","gale","gaze","gazer","glade","goose","gorse","grass",
          "gust","hail","hare","hawk","haze","heart","heather","heron","herring","hill","hollow","hornet","horse",
          "hound","howl","hunt","hunter","ice","ivy","jaguar","jaw","jay","juniper","kite","lake","lark","laurel",
          "leaf","leopard","leap","leaves","leg","legs","lichen","light","lightning","lily","lion","lizard","mallow",
          "maple","marsh","marten","martin","mask","meadow","minnow","mist","moon","moor","moss","mouth","mouse","mud",
          "murk","murmur","muzzle","neck","needle","nettle","night","nose","nut","quail","quill","oak","oath",
          "oleander","owl","pad","patch","patches","paws","peak","pelt","petal","petrel","pigeon","pike","pine","pond",
          "pool","poppy","pounce","puddle","puma","rabbit","rain","raven","reed","ripple","river","roar","rock","rook",
          "root","rose","rowan","runner","rush","rye","sage","sand","scale","scar","scorch","scratch","sedge","seed",
          "shadow","shade","shell","shimmer","shine","shrew","shriek","shrike","sight","skip","sky","slip","smoke",
          "snake","snap","sneeze","snout","snow","song","soot","sorrel","spark","sparrow","speck","speckle","speckles",
          "spider","spirit","splash","spot","spots","spring","spruce","stag","stalk","stem","step","sting","stone",
          "storm","streak","stream","strike","stripe","stump","sun","swan","swift","swoop","tail","talon","tangle",
          "tear","thistle","thorn","throat","thrush","thunder","tiger","toad","tongue","tooth","toe","tree","trot",
          "tuft","tulip","twig","twirl","twist","vine","viper","vixen","vole","wail","walk","walker","warbler","wasp",
          "watcher","water","wave","weed","whisker","whiskers","whisper","willow","wind","wing","wish","wisp","wolf",
          "wood","wren","yarrow","yew"]


def Maingen(pre, suf, m):
    count = 0
    while count < m:
        first = random.choice(pre)
        last = random.choice(suf)
        print(first, last)
        count = count + 1



def isValid(first, last):
    if (first == last) or (first =='silver' and last =='pelt') or (first =='green' and last =='leaf') or \
            (first =='leaf' and last =='fall') or (first =='moon' and (last =='pool' or last =='stone')) or \
            (first =='tall' and (last =='pine' or last == 'rock' )) or (first =='snake' and last =='tongue') or \
            (first =='snake' and last =='tongue'):
        return False
    else:
        return True

max = int(input('Please input how many names you want:'))
Maingen(prefix,suffix, max)
