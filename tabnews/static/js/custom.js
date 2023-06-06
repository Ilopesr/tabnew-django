function detectSystemTheme() {
  const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
  localStorage.setItem('theme', prefersDarkMode ? 'dark' : 'light');
  updateTheme(prefersDarkMode ? 'dark' : 'light');
}

function updateTheme(theme) {
    if(localStorage.getItem('auto-theme') === 'true'){
        $('#switch-light-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
        $('#switch-dark-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
        $("#switch-mode-auto").addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
        if(localStorage.getItem('theme') === 'dark') {
            $("html").removeClass('light').addClass('dark');
            $('#dark-mode .light-mode-icon').hide();
            $('#dark-mode .dark-mode-icon').show();
        } else{
            $("html").removeClass('light').removeClass('dark');
            $('#dark-mode .light-mode-icon').show();
            $('#dark-mode .dark-mode-icon').hide();
        }
    }else if (theme === 'dark') {
    $('#dark-mode').removeClass('light-mode').addClass('dark-mode');
    $("html").removeClass('light').addClass('dark');
    $('#switch-dark-mode').addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    $('#switch-light-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    $("#switch-mode-auto").removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
    $('#dark-mode .light-mode-icon').hide();
    $('#dark-mode .dark-mode-icon').show();
  } else if(theme === 'light') {
    $('#dark-mode').removeClass('dark-mode').addClass('light-mode');
    $("html").removeClass('dark').addClass('light');
    $('#switch-light-mode').addClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    $('#switch-dark-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    $("#switch-mode-auto").removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
    $('#dark-mode .light-mode-icon').show();
    $('#dark-mode .dark-mode-icon').hide();
  }
}

$(document).ready(() => {
  const darkMode = localStorage.getItem('theme');
  const autoThemeEnabled = localStorage.getItem('auto-theme');


  $("#switch-mode-auto").on('click', (e) => {
    e.preventDefault();
    localStorage.setItem('auto-theme', true);
    $('#switch-light-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    $('#switch-dark-mode').removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    $("#switch-mode-auto").addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
    detectSystemTheme();
  });

  if (autoThemeEnabled) {
    detectSystemTheme();
  } else if (darkMode === 'dark') {
    updateTheme('dark');
  } else {
    updateTheme('light');
  }
});

$(".switch-dark-mode").each((index, element) => {
  $(element).on('click', () => {
    if ($(element).attr('id') === 'switch-dark-mode') {
      localStorage.setItem('theme', 'dark');
      localStorage.removeItem('auto-theme');
      updateTheme('dark');
    } else {
      localStorage.setItem('theme', 'light');
      localStorage.removeItem('auto-theme')
      updateTheme('light');
    }
  });
});

$("#dark-mode").on('click', (e) => {
  e.preventDefault();
  const darkMode = $("#dark-mode");
  darkMode.toggleClass("light-mode dark-mode");

  if (darkMode.hasClass('light-mode')) {
    localStorage.setItem('theme', 'light');
    $("html").removeClass('dark');
    localStorage.removeItem('auto-theme');
    darkMode.find('.light-mode-icon').show();
    darkMode.find('.dark-mode-icon').hide();
  } else if (darkMode.hasClass('dark-mode')) {
    localStorage.setItem('theme', 'dark');
    $("html").addClass('dark');
    localStorage.removeItem('auto-theme');
    darkMode.find('.light-mode-icon').hide();
    darkMode.find('.dark-mode-icon').show();
  }
});


