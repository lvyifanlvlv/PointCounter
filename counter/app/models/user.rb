class User < ApplicationRecord
  has_many :counters
	attr_accessor  :reset_token
	before_save { self.email = email.downcase}
	validates :name, presence: true, length: { maximum: 50}
	
	VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
	validates :email,presence: true, length: {maximum: 255},
							format: { with: VALID_EMAIL_REGEX},
							uniqueness: {case_sensitive: false}
	has_secure_password
	validates :password, presence: true, length: { minimum: 6 },allow_nil: true

	# 返回指定字符串的哈希摘要
  def User.digest(string)
    cost = ActiveModel::SecurePassword.min_cost ? BCrypt::Engine::MIN_COST :
                                                  BCrypt::Engine.cost
    BCrypt::Password.create(string, cost: cost)
  end

  	#设置密码重设相关的属性
  def create_reset_digest
    self.reset_token = User.new_token
    update_attribute(:reset_digest,  User.digest(reset_token))
    update_attribute(:reset_sent_at, Time.zone.now)
  end

  	#发送密码重设邮件
  def send_password_reset_email
    UserMailer.password_reset(self).deliver_now
  end

    #返回一个随机令牌
    def User.new_token
      SecureRandom.urlsafe_base64
      
    end

  # 如果指定的令牌和摘要匹配，返回 true
  def authenticated?(attribute, token)
    digest = send("#{attribute}_digest")
    return false if digest.nil?
    BCrypt::Password.new(digest).is_password?(token)
  end


    #如果密码重设请求过期了，返回true
  def password_reset_expired?
    reset_sent_at < 2.hours.ago
  end

  def feed
    Counter.where("user_id = ?",id)
  end
	
end
