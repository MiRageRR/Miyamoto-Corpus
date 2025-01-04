function countCommaSeparatedValues() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var range = sheet.getRange('C3:C300'); // 取得するセルの範囲を指定
  var values = range.getValues();

  // データのカウントを初期化
  var countMap = {};

  // 各セルのデータを処理
  for (var i = 0; i < values.length; i++) {
    for (var j = 0; j < values[i].length; j++) {
      var cellData = values[i][j];
      var items = cellData.split(',');

      // 各アイテムをカウント
      items.forEach(function(item) {
        item = item.trim();
        if (countMap[item]) {
          countMap[item]++;
        } else {
          countMap[item] = 1;
        }
      });
    }
  }

  // 結果を「Count Results」シートに表示
  var resultSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Count Results');
  if (!resultSheet) {
    resultSheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet('Count Results');
  } else {
    // 既存のデータをクリア
    resultSheet.clear();
  }

  // 結果を新しいシートに書き込む
  var row = 1;
  for (var item in countMap) {
    resultSheet.getRange(row, 1).setValue(item);
    resultSheet.getRange(row, 2).setValue(countMap[item]);
    row++;
  }
}