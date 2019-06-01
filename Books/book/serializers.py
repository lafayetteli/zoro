from rest_framework import serializers
from book.models import BookInfo

class HeroSerialisers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hname = serializers.CharField()


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(min_length=3,
                                   max_length=20,
                                   error_messages={
                                       'min_length': '书名必须大于三个字符串',
                                       'max_length': '书名必须少于20个字符串'
                                   }, label='书名', help_text='请输入书名')
    bpub_date = serializers.DateTimeField(write_only= True)
    bread = serializers.IntegerField(min_value=10,max_value=100,required=False)
    bcomment = serializers.IntegerField(min_value=10,max_value=100,required=False)

    def validate_btitle(self,attr):
        if 'django' in attr:
            return attr
        else:
            raise serializers.ValidationError('书名中必须包含django')
    def validate(self, attrs):
        bread = attrs.get('bread')
        comment = attrs.get('comment')
        if all([bread,comment]):
            if bread<comment:
                raise serializers.ValidationError('阅读量必须大于评论量')
        return attrs
    def create(self, validated_data):
        book = BookInfo.objects.create(**validated_data)
        return book
    def update(self, instance, validated_data):
        instance.btitle = validated_data.get('btitle')
        instance.bpub_date = validated_data.get('bpub_date')
        instance.save()
        return instance


class BookModelSerializers(serializers.Serializer):
    heros = HeroSerialisers(serializers.Serializer)
    class Meta():
        module = BookInfo
        fields = ('id','btittle','heros')
        read_only_fields = ('id',)


