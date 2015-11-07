class FNBill(object):
	
	data = {}
	def __init__(self, data):
		membernames = [ 
			"id","chamber", "current_status",
			"bill_number", "state", "session",
			"title", "description", "maybepass_probability",
			"maybepass_date", "maybepass_result", "category_list",		
			"bill_votes", "session_name", "types", 
			"alternate_titles", "bill_companions", "bill_documents",
			"created_at", "updated_at", "current_prediction",
			"bill_similarities", "current_status_date",	"bill_actions",
			"bill_action_dates", "bill_texts", "sources",
			"current_prediction_analysis", "categories", "results",
		]
		for item in data:
			print item[0]
		#for item in membernames:
		#	self.data[item] = data[item]



