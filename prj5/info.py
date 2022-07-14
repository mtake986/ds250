
secThDt = q3.fan.replace({"Yes": "1", 'No': "0"}, inplace=True)
secThDt

secThDt['Location (Census Region)'].replace(
  {
    'South Atlantic': "0", 
    'West South Central': "1", 
    'West North Central': "2",
    'Middle Atlantic': "3", 
    'East North Central': "4", 
    'Pacific': "5",
    'Mountain': "6", 
    'New England': "7", 
    'East South Central': "8"
  }, 
  inplace=True
)
secThDt

secThDt['Which character shot first?'].replace({"I don't understand this question": "-1", "Greedo": "1", "Han": "1"}, inplace=True)

secThDt["FamiliarExpdUniv"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["fanExpdUniv"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["fanStarTrek"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["Gender"].replace({"Male": "1", "Female": "0"}, inplace=True)