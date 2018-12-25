Rails.application.routes.draw do
  get 'password_resets/new'
  get 'password_resets/edit'
  get 'sessions/new'
  get 'users/new'
  root 'static_pages#home'
  get '/help',to: 'static_pages#help'
  get '/about',to: 'static_pages#about'
  get '/contact',to: 'static_pages#contact'
  get '/signup',	to: 'users#new'
  get '/login',		to: 'sessions#new'
  post '/login',	to: 'sessions#create'
  delete '/logout', to:'sessions#destroy'
  post '/signup',	to: 'users#create'
  get  '/ajaxtest' => 'counters#ajaxtest'
  resources :users
  resources :password_resets, only: [:new,:create,:edit,:update]
  resources :counters,          only: [:create,:destroy]
end