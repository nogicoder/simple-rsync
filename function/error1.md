***correction
FFFF.FF

Failures:

  1) rsync core  should copy multiple files to a dir `rsync file1 file2 file3 dir`

       expected: "asvojiibrxaklvhlut\nkdekyrvumfoazocit\nefdyqrnrxbnyjoacptp\ndiewoxdzsthytfic\neswbpwcvomelgxvc\nckmc...ngfnamhgzqbsjlkgn\njndhuotywzvltpbjvuzy\nmtehhkgsdgbkqhnjrszy\nvxaofzrctujqovxq\naxawmmtvxhmhsyfjot"
            got: "uqqomdgzqwkbyerlw\ndlbiwlobcwhyldwiwqbx\nzwpifyuqagllprgdqqzi\nylceaxpknsajfdcnqy\nxxnahtyyjuspxcdnq...nkcoiowhmgaesqigjuzix\nwnismvnqrfshgxcflk\nxjnbdielltsdmlkm\njdelwogyvxjfhlshvu\nwholjmnxgrhblwdkuu"

       (compared using ==)

       Diff:
       @@ -1,23 +1,16 @@
       -asvojiibrxaklvhlut
       -kdekyrvumfoazocit
       -efdyqrnrxbnyjoacptp
       -diewoxdzsthytfic
       -eswbpwcvomelgxvc
       -ckmcjntmgksvwoiv
       -utlemvrfybbmmxikutoz
       -uxqlqnvwtdruxzsu
       -xzpkdhqaafooufltnh
       -fubnyttcapjotcfqhtgj
       -vquwigfcljfgvuzbz
       -mkhakhqpfzqqssdmvx
       -vlapdsbhefpackmn
       -htxzvxulrsapxvxx
       -wcsxrbxyyuhqnlqpb
       -ewelyavvagikpbciota
       -axnogpbhthjfjtzwzd
       -gfnamhgzqbsjlkgn
       -jndhuotywzvltpbjvuzy
       -mtehhkgsdgbkqhnjrszy
       -vxaofzrctujqovxq
       -axawmmtvxhmhsyfjot
       +uqqomdgzqwkbyerlw
       +dlbiwlobcwhyldwiwqbx
       +zwpifyuqagllprgdqqzi
       +ylceaxpknsajfdcnqy
       +xxnahtyyjuspxcdnq
       +cidpaxovyiybzputeslp
       +upeqdzkaujtwteva
       +iclefoezjipvllpbz
       +jltnnetfgvinazyimgtw
       +gezajybgriodnacqsin
       +kcoiowhmgaesqigjuzix
       +wnismvnqrfshgxcflk
       +xjnbdielltsdmlkm
       +jdelwogyvxjfhlshvu
       +wholjmnxgrhblwdkuu

  2) rsync core  should copy multiple files to a dir and keeps permissions and date `rsync file1 file2 file3 dir`

       expected: "uejzlwqntswwqvnfzmnq\nnacpkpgalszuarswtoby\njmwynqiebydelsmelk\nrhdyrjzpeuoencirll\nvdkdrugirhucydtp...dmxinmwtahfltlo\npszjgsjqfyltlpbxauqz\nlswbucgrvgneovkidolt\nbwemhhupupegsmkdfk\nenrmippwuysdzmrepy"
            got: "soolmqlomknszebltsv\nfudomfltbwcaasciibaa\napxmhwndkaigwubcceqy\nqnqlbdzzjsspcmyiziub\ngxmqgorljroza...\nfmllpvyrtwkwoldpngb\nflklworzmdrrxbwti\nqhmxftjkujadirpuomd\nyxrffruihcxvwihnpu\nfmsezzflcimufprk"

       (compared using ==)

       Diff:
       @@ -1,17 +1,33 @@
       -uejzlwqntswwqvnfzmnq
       -nacpkpgalszuarswtoby
       -jmwynqiebydelsmelk
       -rhdyrjzpeuoencirll
       -vdkdrugirhucydtpuaj
       -xtzojypnxskymsjeyy
       -wxkdxrxhjtixavpit
       -mmafammtcuxvogkeo
       -qlsndwyukbnzgoin
       -iasnxufjdtwayebdjn
       -jbnpjrxqcdacqahclk
       -nlfsdmxinmwtahfltlo
       -pszjgsjqfyltlpbxauqz
       -lswbucgrvgneovkidolt
       -bwemhhupupegsmkdfk
       -enrmippwuysdzmrepy
       +soolmqlomknszebltsv
       +fudomfltbwcaasciibaa
       +apxmhwndkaigwubcceqy
       +qnqlbdzzjsspcmyiziub
       +gxmqgorljrozahnjon
       +zsmzlujcjmijxgekub
       +rimoztbxrwyppuuyolm
       +zcpkjxscgynimkywa
       +hahznjkvldbdybbyrm
       +yemtdmhvxskzlhho
       +dfpnucqddmkjxvtf
       +sxryacsbgeaypjcnrckr
       +wtigwumjfwzueiqfwlp
       +qwmehypuriqczjcjtwm
       +nsecnuainqllameq
       +hwixaqcerspgpkyuh
       +uviuvhajriepzjsowpau
       +jdzlrvvgaywptmibzpxb
       +vcktumbnhxzfyuzcygb
       +twtygrcsqohwholr
       +uppxleyobrccsliqwp
       +prrvbmoamewnfgpfyg
       +iuxbhcakvzncmkrzcwh
       +nugmefgfdkkxgbbwv
       +txexhdtyxzsmipaqpmsl
       +fxhzhjpvtnuqunzuoa
       +tldqnwmfdhrcvsbra
       +fmllpvyrtwkwoldpngb
       +flklworzmdrrxbwti
       +qhmxftjkujadirpuomd
       +yxrffruihcxvwihnpu
       +fmsezzflcimufprk

  3) rsync core  should copy multiple files `rsync file1 symlink hardlink dir`

       expected: "kclkrawtiouwjxrx\ngdqdtohzrnqmhhbrckr\notpuwmerpzakxxksz\nxlbznncstdrxaxwj\nzawywmaatzrwatfo\nkbdihhjqxcecridhyck\nnyfzbmrxlbpglldwyln\nhroafjqnivnhterqp"
            got: "abaqwmyqqctquyjbvl\nobrdhthnnenvcllffp\nwbbqbgfbaerufdgz\nucffzjniuipgoxpdfkj\nzmjvxjiwvckzmxgmlge\n...onkrqjvdkbxytnk\nvasjpthaobefhlougm\nyqyrqdrcloprrpgqybis\naqcdbluxqrendorsnvb\nhemchvbiwtcxmmkjoam"

       (compared using ==)

       Diff:
       @@ -1,9 +1,27 @@
       -kclkrawtiouwjxrx
       -gdqdtohzrnqmhhbrckr
       -otpuwmerpzakxxksz
       -xlbznncstdrxaxwj
       -zawywmaatzrwatfo
       -kbdihhjqxcecridhyck
       -nyfzbmrxlbpglldwyln
       -hroafjqnivnhterqp
       +abaqwmyqqctquyjbvl
       +obrdhthnnenvcllffp
       +wbbqbgfbaerufdgz
       +ucffzjniuipgoxpdfkj
       +zmjvxjiwvckzmxgmlge
       +sjqabbaenkljkopri
       +idjamqhrjenfhzsdaszf
       +widdhghsdmxvukxgumk
       +jpofcmqdumuxvzalnp
       +kkirbnzqazwyjomvs
       +syevwzcsxwgbplfqm
       +zhwuipnhadtugybpc
       +ozldngpybjksbuhbw
       +cdryleoaqxjjigmeqjv
       +qnsffvhcgzaspxbgjotk
       +plbssbkmdlrpvkdruwmb
       +bwrcpyxavgkzlmaqlre
       +lepmdjsvqdkllnyrie
       +lvpevrxkjtszdwuy
       +ngsxhyhatckuqnifah
       +mfhjfmvccpftccyqlqp
       +ionkrqjvdkbxytnk
       +vasjpthaobefhlougm
       +yqyrqdrcloprrpgqybis
       +aqcdbluxqrendorsnvb
       +hemchvbiwtcxmmkjoam

  4) rsync core  should copy multiple files to a dir with error in the middle `rsync file1 no_perm_file not_existing_file dir`

     Errno::ENOENT:
       No such file or directory @ rb_sysopen - thwaikahfcpzztxxliko/hqvlwzzfvvcpfcqul***

  **5) rsync core  should copy multiple files `rsync -r dir1/ new_dir`

     Errno::ENOENT:
       No such file or directory @ rb_sysopen - zoqjaooqpbwcxjem/jgkewmlflzuvpzhrjt

  6) rsync core  should copy multiple files `rsync -r dir1/ dir2`

     Errno::ENOENT:
       No such file or directory @ rb_sysopen - rimwtrkliuiomvgureqz/isgsyjzhlwjcjvgqpn**
