var adminApp = angular.module('adminApp', ['ngRoute', 'adminControllers']);

adminApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/dashboard', {
            templateUrl: 'partials/dashboard.html',
            controller: 'dashboardCtl'
        }).when('/pages', {
            templateUrl: 'partials/pages.html',
            controller: 'postsCtl'
        }).when('/posts', {
            templateUrl: 'partials/posts.html',
            controller: 'postsCtl'
        }).when('/posts/:postId', {
            templateUrl: 'partials/edit-post.html',
            controller: 'editPostCtl'
        }).when('/media', {
            templateUrl: 'partials/media.html',
            controller: 'postsCtl'
        }).otherwise({
            redirectTo: '/dashboard'
        });
    }
]);

var adminControllers = angular.module('adminControllers', []);

adminControllers.controller('navbarCtl', ['$scope', '$location',
    function ($scope, $location) {
        $scope.isActive = function (viewLocation) {
            return viewLocation === $location.path();
        };
    }]);

adminControllers.controller('dashboardCtl', ['$scope',
    function ($scope) {
    }]);

adminControllers.controller('pagesCtl', ['$scope',
    function ($scope) {
    }]);

adminControllers.controller('postsCtl', ['$scope',
    function ($scope) {
        $scope.posts = [
            {'title': 'This is a blog post'},
            {'title': 'This is another blog post'},
            {'title': 'A third blog post'}
        ];
    }]);

adminControllers.controller('editPostCtl', ['$scope', '$routeParams',
    function ($scope, $routeParams) {
        $scope.title = "An example post";
        $scope.slug = "an-example-post";
        $scope.id = $routeParams.postId;
    }]);

adminControllers.controller('mediaCtl', ['$scope',
    function ($scope) {
    }]);

