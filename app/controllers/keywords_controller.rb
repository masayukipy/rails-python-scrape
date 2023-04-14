class KeywordsController < ApplicationController    
    # $flag = true
    def index
        @keywords = Keyword.all
    end

    def show
        @keyword = Keyword.find(params[:id])
        @rundates = Rundate.where(word_id: params[:id]).order(date: :asc)
    end

    def new
        @keyword = Keyword.new
    end

    def create
        @keyword = Keyword.new(keyword_params)
        num = params.require(:keyword)["times"].to_i
        arr = Array.new(num)
        if @keyword.save
            while num >= 0
                num -= 1
                arr[num] = {:word_id => @keyword.id, :date => rand(1.months).seconds.from_now, :last_month => 0}
            end
            @rundates = Rundate.create(arr)
            redirect_to @keyword
        else
            render :new, status: :unprocessable_entity
        end

        
    end

    def edit
        @keyword = Keyword.find(params[:id])
    end

    def update
        @keyword = Keyword.find(params[:id])
        num = params.require(:keyword)["times"].to_i
        arr = Array.new(num)
        if @keyword.update(keyword_params)
            @rundate = Rundate.where(word_id: params[:id])
            @rundate.destroy_all
            while num >= 0
                num -= 1
                arr[num] = {:word_id => @keyword.id, :date => rand(1.months).seconds.from_now, :last_month => 0}
            end
            @rundates = Rundate.create(arr)
            redirect_to @keyword
        else
            render :edit, status: :unprocessable_entity
        end
    end

    def destroy
        @keyword = Keyword.find(params[:id])
        @keyword.destroy

        redirect_to @keyword, status: :see_other
    end

    # def run
    #     if $flag
    #         thread = Thread.new { blink_led_constant }
    #         $flag = false
    #     end
    # end

    private
        def keyword_params
            params.require(:keyword).permit(:word, :times)
        end

        # def blink_led_constant
        #     loop do
        #         puts "hello"
        #         sleep(1)
        #     end
        # end


end

