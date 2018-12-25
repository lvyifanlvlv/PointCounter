class User
	attr_accessor :name, :email			#属性访问器存取方法

	def initialize(attributes={})
		@name =attributes[:name]
		@email=attributes[:email]
	end

	def formatted_email
		"#{@name} <#{@email}>"
	end

	def full_name
		"#{@name[:first_name]} #{@name[:last_name]}"
		
	end
end