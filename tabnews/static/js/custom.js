function detectSystemTheme() {
  const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
  localStorage.setItem('theme', prefersDarkMode ? 'dark' : 'light');
  updateTheme(prefersDarkMode ? 'dark' : 'light');
}

function updateTheme(theme) {
  const autoThemeEnabled = localStorage.getItem('auto-theme') === 'true';
  const switchLightMode = $('#switch-light-mode');
  const switchDarkMode = $('#switch-dark-mode');
  const switchModeAuto = $('#switch-mode-auto');
  const darkModeIcon = $('#dark-mode .dark-mode-icon');
  const lightModeIcon = $('#dark-mode .light-mode-icon');
  const htmlElement = $('html');

  if (autoThemeEnabled) {
    switchLightMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    switchDarkMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    switchModeAuto.addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');

    if (theme === 'dark') {
      htmlElement.removeClass('light').addClass('dark');
      darkModeIcon.show();
      lightModeIcon.hide();
    } else {
      htmlElement.removeClass('light dark');
      lightModeIcon.show();
      darkModeIcon.hide();
    }
  } else if (theme === 'dark') {
    $('#dark-mode').removeClass('light-mode').addClass('dark-mode');
    htmlElement.removeClass('light').addClass('dark');
    switchDarkMode.addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    switchLightMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    switchModeAuto.removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
    darkModeIcon.show();
    lightModeIcon.hide();
  } else if (theme === 'light') {
    $('#dark-mode').removeClass('dark-mode').addClass('light-mode');
    htmlElement.removeClass('dark').addClass('light');
    switchLightMode.addClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    switchDarkMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    switchModeAuto.removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');
    lightModeIcon.show();
    darkModeIcon.hide();
  }
}

$(document).ready(() => {
  const darkMode = localStorage.getItem('theme');
  const autoThemeEnabled = localStorage.getItem('auto-theme');

  $("#switch-mode-auto").on('click', (e) => {
    e.preventDefault();
    localStorage.setItem('auto-theme', true);
    const switchLightMode = $('#switch-light-mode');
    const switchDarkMode = $('#switch-dark-mode');
    const switchModeAuto = $("#switch-mode-auto");

    switchLightMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-white bg-opacity-100');
    switchDarkMode.removeClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10');
    switchModeAuto.addClass('ring-[0.0500rem] ring-gray-300 bg-dark bg-opacity-10 auto-switch');

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
    const theme = $(element).attr('id') === 'switch-dark-mode' ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
    localStorage.removeItem('auto-theme');
    updateTheme(theme);
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

$(window).ready(() => {
  const passwordInput = $("#id_password");
  const showPassCheckbox = $("#show-pass");

  showPassCheckbox.prop("checked", false);
  passwordInput.attr("type", "password"); // Ocultar senha
});

const togglePasswordVisibility = () => {
  const passwordInput = $("#id_password");
  const showPassCheckbox = $("#show-pass");

  if (passwordInput.attr("type") === "text") {
    passwordInput.attr("type", "password"); // Ocultar senha
  } else {
    passwordInput.attr("type", "text"); // Exibir senha
  }
};

$(document).ready(function() {
  $('textarea').keydown(function(e) {
    if (e.keyCode == 9) {
      if (e.shiftKey && $(this).is(':focus')) {
        e.preventDefault();
        var start = this.selectionStart;
        var end = this.selectionEnd;
        var value = $(this).val();
        if (value.substring(start - 4, start) == "    ") {
          $(this).val(value.substring(0, start - 4) + value.substring(end));
          this.selectionStart = this.selectionEnd = start - 4;
        }
      } else if ($(this).is(':focus')) {
        e.preventDefault();
        var start = this.selectionStart;
        var end = this.selectionEnd;
        var value = $(this).val();
        $(this).val(value.substring(0, start) + "    " + value.substring(end));
        this.selectionStart = this.selectionEnd = start + 4;
      }
    }
  });
});