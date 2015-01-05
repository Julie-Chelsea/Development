from django.template import Context, TemplateDoesNotExist, TemplateSyntaxError
from django.test import SimpleTestCase

from .test_basic import basic_templates
from ..utils import setup


include_fail_templates = {
    'include-fail1': '{% load bad_tag %}{% badtag %}',
    'include-fail2': '{% load broken_tag %}',
}


class IncludeTagTests(SimpleTestCase):

    @setup({'include01': '{% include "basic-syntax01" %}'}, basic_templates)
    def test_include01(self):
        output = self.engine.render_to_string('include01')
        self.assertEqual(output, 'something cool')

    @setup({'include02': '{% include "basic-syntax02" %}'}, basic_templates)
    def test_include02(self):
        output = self.engine.render_to_string('include02', {'headline': 'Included'})
        self.assertEqual(output, 'Included')

    @setup({'include03': '{% include template_name %}'}, basic_templates)
    def test_include03(self):
        output = self.engine.render_to_string(
            'include03',
            {'template_name': 'basic-syntax02', 'headline': 'Included'},
        )
        self.assertEqual(output, 'Included')

    @setup({'include04': 'a{% include "nonexistent" %}b'})
    def test_include04(self):
        template = self.engine.get_template('include04')

        if self.engine.debug:
            with self.assertRaises(TemplateDoesNotExist):
                template.render(Context({}))
        else:
            output = template.render(Context({}))
            self.assertEqual(output, "ab")

    @setup({
        'include 05': 'template with a space',
        'include06': '{% include "include 05"%}',
    })
    def test_include06(self):
        output = self.engine.render_to_string('include06')
        self.assertEqual(output, "template with a space")

    @setup({'include07': '{% include "basic-syntax02" with headline="Inline" %}'}, basic_templates)
    def test_include07(self):
        output = self.engine.render_to_string('include07', {'headline': 'Included'})
        self.assertEqual(output, 'Inline')

    @setup({'include08': '{% include headline with headline="Dynamic" %}'}, basic_templates)
    def test_include08(self):
        output = self.engine.render_to_string('include08', {'headline': 'basic-syntax02'})
        self.assertEqual(output, 'Dynamic')

    @setup(
        {'include09': '{{ first }}--'
                      '{% include "basic-syntax03" with first=second|lower|upper second=first|upper %}'
                      '--{{ second }}'},
        basic_templates,
    )
    def test_include09(self):
        output = self.engine.render_to_string('include09', {'first': 'Ul', 'second': 'lU'})
        self.assertEqual(output, 'Ul--LU --- UL--lU')

    @setup({'include10': '{% include "basic-syntax03" only %}'}, basic_templates)
    def test_include10(self):
        output = self.engine.render_to_string('include10', {'first': '1'})
        if self.engine.string_if_invalid:
            self.assertEqual(output, 'INVALID --- INVALID')
        else:
            self.assertEqual(output, ' --- ')

    @setup({'include11': '{% include "basic-syntax03" only with second=2 %}'}, basic_templates)
    def test_include11(self):
        output = self.engine.render_to_string('include11', {'first': '1'})
        if self.engine.string_if_invalid:
            self.assertEqual(output, 'INVALID --- 2')
        else:
            self.assertEqual(output, ' --- 2')

    @setup({'include12': '{% include "basic-syntax03" with first=1 only %}'}, basic_templates)
    def test_include12(self):
        output = self.engine.render_to_string('include12', {'second': '2'})
        if self.engine.string_if_invalid:
            self.assertEqual(output, '1 --- INVALID')
        else:
            self.assertEqual(output, '1 --- ')

    @setup(
        {'include13': '{% autoescape off %}{% include "basic-syntax03" %}{% endautoescape %}'},
        basic_templates,
    )
    def test_include13(self):
        output = self.engine.render_to_string('include13', {'first': '&'})
        if self.engine.string_if_invalid:
            self.assertEqual(output, '& --- INVALID')
        else:
            self.assertEqual(output, '& --- ')

    @setup(
        {'include14': '{% autoescape off %}'
                      '{% include "basic-syntax03" with first=var1 only %}'
                      '{% endautoescape %}'},
        basic_templates,
    )
    def test_include14(self):
        output = self.engine.render_to_string('include14', {'var1': '&'})
        if self.engine.string_if_invalid:
            self.assertEqual(output, '& --- INVALID')
        else:
            self.assertEqual(output, '& --- ')

    # Include syntax errors
    @setup({'include-error01': '{% include "basic-syntax01" with %}'})
    def test_include_error01(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error01')

    @setup({'include-error02': '{% include "basic-syntax01" with "no key" %}'})
    def test_include_error02(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error02')

    @setup({'include-error03': '{% include "basic-syntax01" with dotted.arg="error" %}'})
    def test_include_error03(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error03')

    @setup({'include-error04': '{% include "basic-syntax01" something_random %}'})
    def test_include_error04(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error04')

    @setup({'include-error05': '{% include "basic-syntax01" foo="duplicate" foo="key" %}'})
    def test_include_error05(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error05')

    @setup({'include-error06': '{% include "basic-syntax01" only only %}'})
    def test_include_error06(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-error06')

    @setup(include_fail_templates)
    def test_include_fail1(self):
        with self.assertRaises(RuntimeError):
            self.engine.get_template('include-fail1')

    @setup(include_fail_templates)
    def test_include_fail2(self):
        with self.assertRaises(TemplateSyntaxError):
            self.engine.get_template('include-fail2')

    @setup({'include-error07': '{% include "include-fail1" %}'}, include_fail_templates)
    def test_include_error07(self):
        template = self.engine.get_template('include-error07')

        if self.engine.debug:
            with self.assertRaises(RuntimeError):
                template.render(Context())
        else:
            self.assertEqual(template.render(Context()), '')

    @setup({'include-error08': '{% include "include-fail2" %}'}, include_fail_templates)
    def test_include_error08(self):
        template = self.engine.get_template('include-error08')

        if self.engine.debug:
            with self.assertRaises(TemplateSyntaxError):
                template.render(Context())
        else:
            self.assertEqual(template.render(Context()), '')

    @setup({'include-error09': '{% include failed_include %}'}, include_fail_templates)
    def test_include_error09(self):
        context = Context({'failed_include': 'include-fail1'})
        template = self.engine.get_template('include-error09')

        if self.engine.debug:
            with self.assertRaises(RuntimeError):
                template.render(context)
        else:
            self.assertEqual(template.render(context), '')

    @setup({'include-error10': '{% include failed_include %}'}, include_fail_templates)
    def test_include_error10(self):
        context = Context({'failed_include': 'include-fail2'})
        template = self.engine.get_template('include-error10')

        if self.engine.debug:
            with self.assertRaises(TemplateSyntaxError):
                template.render(context)
        else:
            self.assertEqual(template.render(context), '')
