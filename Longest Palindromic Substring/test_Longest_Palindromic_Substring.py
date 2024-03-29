import unittest
from Longest_Palindromic_Substring import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_character(self):
        s = "a"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_two_characters(self):
        s = "ab"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "bb"
        expect = "bb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_three_characters(self):
        s = "aba"
        expect = "aba"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abc"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "aab"
        expect = "aa"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abb"
        expect = "bb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_four_characters(self):
        s = "abba"
        expect = "abba"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abaa"
        expect = "aba"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abab"
        expect = "aba"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abbb"
        expect = "bbb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "aabb"
        expect = "aa"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "acbb"
        expect = "bb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abbc"
        expect = "bb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abcd"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_leetcode_tleStr(self):
        # 20 / 140 test cases passed. Status: Time Limit Exceeded.
        tleStr = "abbcccbbbcaaccbababcbcabca"
        expect = "bbcccbb"
        self.assertEqual(expect, self.solution.longestPalindrome(tleStr))

        # 104 / 140 test cases passed. Status: Time Limit Exceeded
        tleStr = "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftvhpdgjjfafunfndztdjkcxyihtsyppendfzzjeyxlbwpdygiqmdqcdbmgyjigrmfkswcwryaydjilqqxvcnyvviesuncslvzikawwqykqwdfibggezufqihcjkebapmgkvwixywgdextafxycnipjglsndkyjoqfyfljfkkvoieksmavdlmlhhnstesibffiopqvlyuidvrawndbzonwzbsjmpeqoglmdbinkovqpzfkxihzitdopnomseqhmrrkcsvrzziphwpuhjngeotwcrebcmbtirkgeavojtmpakcewmexhxacngknokxsvtqobdgckutpexswgwqzbosjpxauyflnylfcxsucsehqvakbpvfmkelmkspsqxnutwfwacpqqvovdqafeylobneojdsgqowcbxfsvuqusdbylcgcvgrofgvzubakjmlbffjhrafvnqttwuyhokzpmhlludpbowuxzrebxsdusalljfjgjkucwzpmndqncykvfnbrxcrcaxwisjpstejjqbpwegpxyrtyafxklgralnkwxkmjpuqfixzkonznmguyizlancpxdzcfkgiotyelegprbaytdhbutbuihkxnbtuqrtezaskfqsmrznfohhlqp"
        expect = "zqz"
        self.assertEqual(expect, self.solution.longestPalindrome(tleStr))

        # 118 / 140 test cases passed. Status: Time Limit Exceeded
        tleStr = "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"
        expect = "byyb"
        self.assertEqual(expect, self.solution.longestPalindrome(tleStr))

        # 133 / 140 test cases passed. Status: Time Limit Exceeded
        tleStr = "borcdubqiupahpwjizjjbkncelfazeqynfbrnzuvbhjnyvrlkdyfyjjxnprfocrmisugizsgvhszooktdwhehojbrdbtgkiwkhpfjfcstwcajiuediebdhukqnroxbgtvottummbypokdljjvnthcbesoyigscekrqswdpalnjnhcnqrarxuufzzmkwizptyvjhpfidgmskuaggtpxqisdlyloznkarxofzeeyvteynluofuhbllyiszszbwnsglqjkignusarxsjvctpgiwnhdufmfpanfwxjwlmhgllzsmdpncbwnsbdtsvrjybynifywkulqnzprcxockbhrhvnwxrkvwumyieazclcviumvormynbryaziijpdinwatwqppamfiqfiojgwkvfzyxadyfjrgmtttvlgkqghgbcfhkigfojjkhskzenlpasyozcsuccdxhulcubsgomvcrbqwakrraesfifecmoztayrdjicypakrrneulfbqqxtrdelggedvloebqaztmfyfkhuonrognejxpesmwgnmnnnamvkxqvzrgzdqtvuhccryeowywmbixktnkqnwzlzfvloyqcageugmjqihyjxhssmhkfzxpzxmgpjgsduogfolnkkqizitbvvgrkczmojxnabruwwzxxqcevdwvtiigwckpxnnxxxdhxpgomncttjutrsvyrqcfwxhexhaguddkiesmfrqfjfdaqbkeqinwicphktffuwcazlmerdhraufbpcznbuipmymipxbsdhuesmcwnkdvilqbnkaglloswcpqzdggnhjdkkumfuzihilrpcvemwllicoqiugobhrwdxtoefynqmccamhdtxujfudbglmiwqklriolqfkknbmindxtljulnxhipsieyohnczddabrxzjmompbtnnxvivmoyfzfrxlufowtqzojfclmatthjtbhotdoheusnpirwicbtyrcuojsdmfcx"
        expect = "xnnx"
        self.assertEqual(expect, self.solution.longestPalindrome(tleStr))

    def test_leetcode_wa(self):
        s = "babad"
        expect = "bab"
        self.assertEqual(expect, self.solution.longestPalindrome(s))


if __name__ == '__main__':
    unittest.main()
