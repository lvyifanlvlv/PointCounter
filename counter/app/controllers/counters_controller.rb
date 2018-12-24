class CountersController < ApplicationController
	before_action :logged_in_user, only: [:create,:destroy]
  before_action :correct_user,   only: :destroy

  	def create
  		@counter = current_user.counters.build(counter_params)
  		if @counter.save
  			flash[:success]="Please wait..."
  			redirect_to root_url
  		else
        @feed_items = []
  			render 'static_pages/home'
      end
  	end

  	def destroy
      @counter.destroy
      flash[:success] = "Counter deleted"
      redirect_to request.referrer || root_url
  	end

  	private

    def counter_params
      params.require(:counter).permit(:content,:picture)
    end

    def correct_user
      @counter = current_user.counters.find_by(id: params[:id])
      redirect_to root_url if @counter.nil?
    end
end

