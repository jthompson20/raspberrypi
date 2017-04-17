class User < ApplicationRecord
	before_save { self.email = email.downcase }
	validates :first, 		presence: true, length: { maximum: 50 }
	validates :last, 		presence: true, length: { maximum: 50 }
	validates :email, 		
		presence: true, 
		length: { maximum: 255 }, 
		format: { with: /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i }, 
		uniqueness: true
	validates :username, 	presence: true, length: { maximum: 50 }, uniqueness: true
	validates :active, 		presence: true
	validates :admin, 		presence: true
	has_secure_password
end
