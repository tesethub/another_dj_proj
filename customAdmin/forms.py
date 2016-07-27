from django.forms import ModelForm


def form_construct(Model):
    class AnotherForm(ModelForm):
        class Meta:
            model=Model
            fields='__all__'

    return AnotherForm





