Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  root "keywords#index"
  get "/keywords/run", to: "keywords#run"
  resources :keywords
end
