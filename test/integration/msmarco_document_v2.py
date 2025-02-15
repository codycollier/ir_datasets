import re
import unittest
from ir_datasets.datasets.msmarco_document_v2 import MsMarcoV2Document
from ir_datasets.formats import GenericQuery, TrecQrel, GenericScoredDoc
from .base import DatasetIntegrationTest


class TestMsMarcoDocumentV2(DatasetIntegrationTest):
    def test_docs(self):
        self._test_docs('msmarco-document-v2', count=11959635, items={
            0: MsMarcoV2Document('msmarco_doc_00_0', 'http://0-60.reviews/0-60-times/', '0-60 Times - 0-60 | 0 to 60 Times & 1/4 Mile Times | Zero to 60 Car Reviews', '0-60 Times\n0-60 Times', re.compile('^0\\-60 Times \\- 0\\-60 \\| 0 to 60 Times \\& 1/4 Mile Times \\| Zero to 60 Car Reviews\n0\\-60 Times\nThere are man.{4332} biggest touted numbers for vehicles, and easier for people to relate to than horsepower and torque\\.$', flags=48)),
            9: MsMarcoV2Document('msmarco_doc_00_89242', 'http://001yourtranslationservice.com/translating/translation-tips/translator-translation-rates-charges-prices.html', '', '\n', re.compile('^Translator or Translation Rates Charges, Prices and Fees\nBasic guideline to what other translators a.{24817}without hunting down their\naddresses on the net\\.\nTranslator Application\\- come join our growing team!$', flags=48)),
            11959634: MsMarcoV2Document('msmarco_doc_59_1043776256', 'https://zzzzbov.com/blag/shortcut-to-zoom', 'Shortcut to Zoom › zzzzBov.com', 'Shortcut to Zoom\nShortcut to Zoom\nBatch File\nShortcut\nTrying it out\n', re.compile('^Shortcut to Zoom › zzzzBov\\.com\n07 \\- Apr \\- 2020\nShortcut to Zoom\nI use Chrome on Windows as my primar.{2297}hat adding even a few of these to my start menu will help reduce just a bit more friction in my day\\.$', flags=48)),
        })

    def test_queries(self):
        self._test_queries('msmarco-document-v2/train', count=322196, items={
            0: GenericQuery('121352', 'define extreme'),
            9: GenericQuery('918533', 'what was introduced to the human diet in what year'),
            322195: GenericQuery('50393', 'benefits of boiling lemons and drinking juice.'),
        })
        self._test_queries('msmarco-document-v2/dev1', count=4552, items={
            0: GenericQuery('2', ' Androgen receptor define'),
            9: GenericQuery('873886', 'what level does zubat evolves to'),
            4551: GenericQuery('1048565', 'who plays sebastian michaelis'),
        })
        self._test_queries('msmarco-document-v2/dev2', count=5000, items={
            0: GenericQuery('1048579', 'what is pcnt'),
            9: GenericQuery('1048779', 'what is ott media'),
            4999: GenericQuery('1092262', ';liter chemistry definition'),
        })
        self._test_queries('msmarco-document-v2/trec-dl-2019', count=200, items={
            0: GenericQuery('1108939', 'what slows down the flow of blood'),
            9: GenericQuery('885490', 'what party is paul ryan in'),
            199: GenericQuery('532603', 'university of dubuque enrollment'),
        })
        self._test_queries('msmarco-document-v2/trec-dl-2019/judged', count=43, items={
            0: GenericQuery('156493', 'do goldfish grow'),
            9: GenericQuery('915593', 'what types of food can you cook sous vide'),
            42: GenericQuery('146187', 'difference between a mcdouble and a double cheeseburger'),
        })
        self._test_queries('msmarco-document-v2/trec-dl-2020', count=200, items={
            0: GenericQuery('1030303', 'who is aziz hashim'),
            9: GenericQuery('1071750', 'why is pete rose banned from hall of fame'),
            199: GenericQuery('132622', 'definition of attempted arson'),
        })
        self._test_queries('msmarco-document-v2/trec-dl-2020/judged', count=45, items={
            0: GenericQuery('1030303', 'who is aziz hashim'),
            9: GenericQuery('1105792', 'define: geon'),
            44: GenericQuery('997622', 'where is the show shameless filmed'),
        })

    def test_qrels(self):
        self._test_qrels('msmarco-document-v2/train', count=331956, items={
            0: TrecQrel('10000', 'msmarco_doc_10_1691063043', 1, '0'),
            9: TrecQrel('1000015', 'msmarco_doc_03_889237013', 1, '0'),
            331955: TrecQrel('999999', 'msmarco_doc_19_673141443', 1, '0'),
        })
        self._test_qrels('msmarco-document-v2/dev1', count=4702, items={
            0: TrecQrel('1000000', 'msmarco_doc_17_2560009121', 1, '0'),
            9: TrecQrel('1000459', 'msmarco_doc_01_1739820096', 1, '0'),
            4701: TrecQrel('999942', 'msmarco_doc_06_956348348', 1, '0'),
        })
        self._test_qrels('msmarco-document-v2/dev2', count=5178, items={
            0: TrecQrel('1000202', 'msmarco_doc_08_73026062', 1, '0'),
            9: TrecQrel('1000748', 'msmarco_doc_17_1575450501', 1, '0'),
            5177: TrecQrel('999937', 'msmarco_doc_05_319743607', 1, '0'),
        })
        self._test_qrels('msmarco-document-v2/trec-dl-2019', count=13940, items={
            0: TrecQrel('19335', 'msmarco_doc_15_774111471', 0, 'Q0'),
            9: TrecQrel('19335', 'msmarco_doc_02_1452351439', 0, 'Q0'),
            13939: TrecQrel('1133167', 'msmarco_doc_39_1213201840', 0, 'Q0'),
        })
        self._test_qrels('msmarco-document-v2/trec-dl-2019/judged', count=13940, items={
            0: TrecQrel('19335', 'msmarco_doc_15_774111471', 0, 'Q0'),
            9: TrecQrel('19335', 'msmarco_doc_02_1452351439', 0, 'Q0'),
            13939: TrecQrel('1133167', 'msmarco_doc_39_1213201840', 0, 'Q0'),
        })
        self._test_qrels('msmarco-document-v2/trec-dl-2020', count=7942, items={
            0: TrecQrel('42255', 'msmarco_doc_05_401511459', 0, '0'),
            9: TrecQrel('42255', 'msmarco_doc_10_1361976246', 0, '0'),
            7941: TrecQrel('1136962', 'msmarco_doc_51_164249476', 0, '0'),
        })
        self._test_qrels('msmarco-document-v2/trec-dl-2020/judged', count=7942, items={
            0: TrecQrel('42255', 'msmarco_doc_05_401511459', 0, '0'),
            9: TrecQrel('42255', 'msmarco_doc_10_1361976246', 0, '0'),
            7941: TrecQrel('1136962', 'msmarco_doc_51_164249476', 0, '0'),
        })

    def test_scoreddocs(self):
        self._test_scoreddocs('msmarco-document-v2/train', count=32218809, items={
            0: GenericScoredDoc('3', 'msmarco_doc_22_449579381', 12.0778),
            9: GenericScoredDoc('3', 'msmarco_doc_26_1982585323', 11.798),
            32218808: GenericScoredDoc('1185869', 'msmarco_doc_31_166994410', 9.1289),
        })
        self._test_scoreddocs('msmarco-document-v2/dev1', count=455200, items={
            0: GenericScoredDoc('2', 'msmarco_doc_40_297326624', 12.3384),
            9: GenericScoredDoc('2', 'msmarco_doc_53_358317456', 11.702),
            455199: GenericScoredDoc('1102390', 'msmarco_doc_35_112595707', 7.2917),
        })
        self._test_scoreddocs('msmarco-document-v2/dev2', count=500000, items={
            0: GenericScoredDoc('361', 'msmarco_doc_46_1474316753', 6.7154),
            9: GenericScoredDoc('361', 'msmarco_doc_46_1474322309', 6.5316),
            499999: GenericScoredDoc('1102413', 'msmarco_doc_51_471353527', 9.8727),
        })


if __name__ == '__main__':
    unittest.main()
