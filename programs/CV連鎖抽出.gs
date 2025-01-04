function extractCVChains() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var range = sheet.getDataRange();
  var values = range.getValues();

  // 子音と母音のリストを定義
  var consonants1 = ['p', 'b', 't', 'g', 'k', 's', 'ʃ', 'tʃ', 'dʒ', 'ɾ', 'm', 'n', 'h', 'j', 'd'];
  var consonants2 = ['z', 'ʒ', 'θ', 'ð', 'l', 'ŋ', 'w', 'f', 'v'];
  var vowels1 = ['o', 'i', 'e'];
  var vowels2 = ['æ', 'ʌ', 'ǝ', 'u', 'ʊ', 'ɪ', 'ɛ', 'a','ɔ','ɑ'];

  // 正規表現パターンを定義
  var cvPattern = /([pbtdkgɡsvfzʃʒmnŋlrwjhθðʧʤ])([aeiouæɔəɛɪʊʌɒɑ])/g;

  for (var i = 2; i < values.length; i++) {
    var text = values[i][1]; // 左隣のセルから文章を読み込む
    Logger.log('Row ' + (i + 1) + ' Text: ' + text); // インポートされた文章をログに出力

    var matches = [];
    var match;
    while ((match = cvPattern.exec(text)) !== null) {
      var consonant = match[1];
      var vowel = match[2];
      // 子音①と母音①の組み合わせを除外
      if (!(consonants1.includes(consonant) && vowels1.includes(vowel))) {
        matches.push(consonant + vowel); // 子音と母音のペアを連結して保存
      }
    }
    Logger.log('Row ' + (i + 1) + ' Matches: ' + matches); // 抽出されたCV連鎖をログに出力

    values[i][2] = matches.join(", "); // CV連鎖を右隣のセルに表示
    Logger.log('Row ' + (i + 1) + ' CV Chains: ' + values[i][2]); // 結果をログに出力
  }

  sheet.getRange(1, 1, values.length, values[0].length).setValues(values);
}
