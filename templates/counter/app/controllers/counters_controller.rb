class CountersController < ApplicationController
	before_action :logged_in_user, only: [:create,:destroy]
  before_action :correct_user,   only: :destroy

  	def create
      puts "======================"
     puts counter_params
      puts "======================"
  		@counter = current_user.counters.build(counter_params)
  		if @counter.save
  			flash.now[:success]="Please wait..."
  			redirect_to root_url
  		else
        @feed_items = []
  			render 'static_pages/home'
      end
  	end

  	def destroy
      @counter.destroy
      flash.now[:success] = "Successfully deleted!"
      redirect_to request.referrer || root_url
  	end

    def ajaxtest
      #向后端发送计数请求
    end

  	private

    def counter_params
      params.require(:counter).permit(:content,:picture,:studentnumber,:studentname,:projectname)
    end

    def correct_user
      @counter = current_user.counters.find_by(id: params[:id])
      redirect_to root_url if @counter.nil?
    end
end

