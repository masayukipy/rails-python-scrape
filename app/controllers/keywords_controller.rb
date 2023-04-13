class KeywordsController < ApplicationController
    def index
        @keywords = Keyword.all
    end

    def show
        @keyword = Keyword.find(params[:id])
        @rundates = Rundate.where(word_id: params[:id])
    end

    def new
        @keyword = Keyword.new
    end

    def create
        @keyword = Keyword.new(keyword_params)
        logger.info("sssssssssssssssssssssssssssssssss")
        logger.info(params.require(:keyword))
        # rows = Array.new(keyword_params.times)
        if @keyword.save
            # @rundates = Rundate.create(
            #     [
            #         {:word_id => @keyword.id, :run_date => rand(1.months).seconds.from_now, :status => false},
            #         {:word_id => @keyword.id, :run_date => rand(1.months).seconds.from_now, :status => false},
            #         {:word_id => @keyword.id, :run_date => rand(1.months).seconds.from_now, :status => false},
            #         {:word_id => @keyword.id, :run_date => rand(1.months).seconds.from_now, :status => false},
            #         {:word_id => @keyword.id, :run_date => rand(1.months).seconds.from_now, :status => false}
            #     ]
            # )
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

        if @keyword.update(keyword_params)
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

    private
        def keyword_params
            params.require(:keyword).permit(:word, :times)
        end
end

