import rhinoMorph

rn = rhinoMorph.startRhino()

text = "한글로 된 한글텍스트를 분석하는 것은 즐겁다."

text_analyzed = rhinoMorph.onlyMorph_list(rn, text)

print('1. 형태소 분석 결과:', text_analyzed)