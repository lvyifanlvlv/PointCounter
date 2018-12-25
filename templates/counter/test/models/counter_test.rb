require 'test_helper'

class CounterTest < ActiveSupport::TestCase
  def setup
    @user = users(:michael)
    # 这行代码不符合常见做法
    @counter = Counter.new(content: "Lorem ipsum", user_id: @user.id)
  end

  test "should be valid" do
    assert @counter.valid?
  end

  test "user id should be present" do
    @counter.user_id = nil
    assert_not @counter.valid?
  end

 # test "content should be present" do
  #  @counter.content = "   "
   # assert_not @counter.valid?
  #end



end
